import scrapy
import re

class ImdbSpider(scrapy.Spider):
    name = "imdb_spider"
    allowed_domains = ["www.imdb.com"]
    start_urls = [
        'https://www.imdb.com/search/title/?title_type=feature&genres=adventure',
    ]

    def parse(self, response):
        if response.status == 200:
            self.logger.info("Début extraction")
            for film in response.css('.ipc-metadata-list'):
                for i in range(1, 25):
                    try:
                        self.logger.info(f"Traitement du film {i}")
                        item = self.extract_movie_information(film, i)
                        if item:
                            yield item
                    except Exception as e:
                        self.logger.error(f"Erreur lors du traitement d'un film : {e}")

        # Pour gérer la pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def extract_movie_information(self, film, index):
        # Fonction pour extraire toutes les informations d'un film
        try:
            title = self.remove_number_before_dot(self.extract_title(film, index))
            url =  self.extract_url(film, index)
            year = self.extract_year(film, index)
            time = self.extract_duration(film, index)
            resume = self.extract_summary(film, index)
            score = self.extract_score(film, index)

            item = {
                'titre': title,
                'annee_sortie': year,
                'duree': time,
                'resume': resume,
                'metascore': score,
                'lien': url,
            }
            self.logger.info(f"Film traité : {item}")
            return item
        except Exception as e:
            self.logger.error(f"Erreur lors de l'extraction des informations du film : {e}")
            return None

    def extract_title(self, film, index):
        # Extraction du titre du film
        a_element = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1)').get()
        selector = scrapy.Selector(text=a_element)
        return selector.xpath('.//text()').get()

    def extract_url(self, film, index):
        # Extraction de l'URL de la page détaillée du film
        a_element = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)').get()
        selector = scrapy.Selector(text=a_element)
        return "https://www.imdb.com" + selector.css('a::attr(href)').get()

    def extract_year(self, film, index):
        # Extraction de l'année de sortie du film
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()

    def extract_duration(self, film, index):
        # Extraction de la durée du film
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()

    def extract_summary(self, film, index):
        # Extraction du résumé du film
        div_html = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)').get()
        selector = scrapy.Selector(text=div_html)
        return selector.xpath('.//text()').get()

    def extract_score(self, film, index):
        # Extraction du score du film
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(4) > span:nth-child(1)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()


    def remove_number_before_dot(self, text):
        # Supprime le numéro de classement (ex: "1. ") au début du titre
        return re.sub(r'^\d+\.\s', '', text)

    def escape_csv_field(self, text):
        # Échapper correctement les champs pour le format CSV
        if text is None:
            return ""
        # Remplacer les guillemets par des doubles guillemets
        text = text.replace('"', '""')
        # Si le texte contient des virgules, des guillemets ou des sauts de ligne, l'entourer de guillemets
        if ',' in text or '"' in text or '\n' in text or '\r' in text:
            text = f'"{text}"'
        return text
