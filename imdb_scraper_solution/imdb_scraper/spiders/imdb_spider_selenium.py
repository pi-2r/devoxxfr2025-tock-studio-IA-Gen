import scrapy
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from scrapy.http import HtmlResponse

class ImdbSpiderSelenium(scrapy.Spider):
    name = "imdb_spider_selenium"
    allowed_domains = ["www.imdb.com"]
    start_urls = [
        'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
    ]

    def __init__(self, *args, **kwargs):
        super(ImdbSpider, self).__init__(*args, **kwargs)
        # Configuration du webdriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
        self.driver = webdriver.Chrome(options=options)

    def parse(self, response):
        # Utiliser Selenium pour charger la page
        self.driver.get(response.url)
        self.logger.info(f"Page chargée: {response.url}")

        # Attendre que la page soit complètement chargée
        time.sleep(5)

        # Nombre de fois à cliquer sur "50 en plus"
        click_count = 5

        # XPath exact du bouton fourni par l'utilisateur
        button_xpath = "/html/body/div[2]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/div[2]/div/span/button"

        for i in range(click_count):
            try:
                # Faire défiler jusqu'en bas de la page pour s'assurer que le bouton est chargé
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)

                # Attendre que le bouton soit présent dans le DOM
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, button_xpath))
                )

                # Trouver le bouton avec le XPath exact
                load_more_button = self.driver.find_element(By.XPATH, button_xpath)

                # Faire défiler jusqu'au bouton pour s'assurer qu'il est visible
                self.driver.execute_script("arguments[0].scrollIntoView(true);", load_more_button)
                time.sleep(1)

                # Vérifier si le bouton est cliquable
                if load_more_button.is_displayed() and load_more_button.is_enabled():
                    # Cliquer sur le bouton
                    load_more_button.click()
                    self.logger.info(f"Clic #{i+1} sur le bouton '50 en plus'")

                    # Attendre le chargement des nouveaux éléments
                    time.sleep(5)
                else:
                    # Si le bouton n'est pas cliquable, essayer de cliquer via JavaScript
                    self.logger.info("Bouton trouvé mais non cliquable, tentative via JavaScript")
                    self.driver.execute_script("arguments[0].click();", load_more_button)
                    time.sleep(5)

            except Exception as e:
                self.logger.error(f"Erreur lors du clic sur le bouton (tentative {i+1}): {e}")
                # Prendre une capture d'écran pour le débogage
                self.driver.save_screenshot(f'error_click_{i+1}.png')

                # Essayer une approche alternative avec JavaScript
                try:
                    self.logger.info("Tentative alternative avec JavaScript")
                    clicked = self.driver.execute_script("""
                        var buttons = document.querySelectorAll('button');
                        for (var i = 0; i < buttons.length; i++) {
                            if (buttons[i].textContent.includes('50 en plus')) {
                                buttons[i].click();
                                return true;
                            }
                        }
                        return false;
                    """)
                    if clicked:
                        self.logger.info("Clic réussi via JavaScript")
                        time.sleep(5)
                    else:
                        self.logger.warning("Bouton '50 en plus' non trouvé via JavaScript")
                except Exception as js_error:
                    self.logger.error(f"Erreur lors de la tentative JavaScript: {js_error}")
                    break

        # Créer une nouvelle réponse à partir du contenu de la page après les clics
        self.logger.info("Extraction des données de la page mise à jour")
        updated_response = HtmlResponse(
            url=response.url,
            body=self.driver.page_source.encode('utf-8'),
            encoding='utf-8'
        )

        # Extraction des films avec la page mise à jour
        films = updated_response.css('.ipc-metadata-list-summary-item')
        self.logger.info(f"Nombre de films trouvés: {len(films)}")

        for i, film in enumerate(films, 1):
            try:
                self.logger.info(f"Traitement du film {i}")
                item = self.extract_film_info(film)
                if item:
                    yield item
            except Exception as e:
                self.logger.error(f"Erreur lors du traitement du film {i}: {e}")

    def extract_film_info(self, film):
        try:
            # Extraction avec des sélecteurs plus robustes
            title = film.css('h3.ipc-title__text::text').get()
            if title:
                title = title.strip()
                # Supprimer les numéros au début (ex: "1. Film Title")
                title = re.sub(r'^\d+\.\s*', '', title)

            url = film.css('a.ipc-title-link-wrapper::attr(href)').get()
            if url:
                url = "https://www.imdb.com" + url

            # Extraction des métadonnées
            metadata_items = film.css('.dli-title-metadata-item::text').getall()
            year = metadata_items[0].strip() if len(metadata_items) > 0 else None
            time = metadata_items[1].strip() if len(metadata_items) > 1 else None

            resume = film.css('.ipc-html-content-inner-div::text').get()
            if not resume:
                resume = film.css('.ipc-html-content-inner-div p::text').get()

            score = film.css('.ipc-rating-star--imdb::text').get()
            if score:
                score = score.strip()

            item = {
                'titre': title,
                'annee_sortie': year,
                'duree': time,
                'resume': resume,
                'metascore': score,
                'lien': url,
            }
            return item
        except Exception as e:
            self.logger.error(f"Erreur lors de l'extraction des informations du film : {e}")
            return None

    def closed(self, reason):
        # Fermer le navigateur à la fin
        self.driver.quit()
