#  Scrapping de données et RAG

[<img src="img/Indiana-jones-and-the-dial-of-destiny.jpg"  alt="Indiana-jones-and-the-dial-of-destiny">](https://www.youtube.com/watch?v=tI6HUqCDKvw)

> "Get Back", Indiana Jones and the Dial of Destiny, Steven Spielberg, 2023


<br/>
<u>Objectifs:</u>

- Découvrir le scraping de données
- Installer et jouer avec le Framework Scrapy
- Débloquer les 1er protections anti-bot
- Extraires des données d'un site web au format CSV
- Allez plus loin avec le système de proxy


## Sommaire

- [Installer le framework Scrapy](#installer-le-framework-scrapy)
- [Extraire les informations souhaitées](#extraire-les-informations-souhaitées)
- [Contourner les 1er protections anti-bot](#contourner-les-1er-protections-anti-bot)
  
- 
Pour scraper la page IMDb avec Scrapy et extraire les informations souhaitées, vous devez suivre ces étapes:

## Installer le framework Scrapy
Installer Scrapy : Assurez-vous d'avoir Python 3 installé, puis installez Scrapy en utilisant pip:

```bash
pip install Scrapy
```
Créer un nouveau projet Scrapy :

```bash
scrapy startproject imdb_scraper
```
Naviguer vers le dossier du projet :

```bash
cd imdb_scraper
```
Créer un nouveau Spider :

```bash
scrapy genspider imdb_spider imdb.com
```

## Extraire les informations souhaitées
Ouvrez le fichier `imdb_spider.py` et ajoutez le code suivant pour extraire les informations souhaitées:

```python
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
                        item = self.extract_film_info(film, i)
                        if item:
                            yield item
                    except Exception as e:
                        self.logger.error(f"Erreur lors du traitement d'un film : {e}")

        # Pour gérer la pagination
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def extract_film_info(self, film, index):
        try:
            title = self.extract_title(film, index)
            url = self.extract_url(film, index)
            year = self.extract_year(film, index)
            time = self.extract_time(film, index)
            resume = self.extract_resume(film, index)
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
        a_element = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1)').get()
        selector = scrapy.Selector(text=a_element)
        return selector.xpath('.//text()').get()

    def extract_url(self, film, index):
        a_element = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > a:nth-child(3)').get()
        selector = scrapy.Selector(text=a_element)
        return "https://www.imdb.com" + selector.css('a::attr(href)').get()

    def extract_year(self, film, index):
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()

    def extract_time(self, film, index):
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()

    def extract_resume(self, film, index):
        div_html = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)').get()
        selector = scrapy.Selector(text=div_html)
        return selector.xpath('.//text()').get()

    def extract_score(self, film, index):
        span_text = film.css(f'li.ipc-metadata-list-summary-item:nth-child({index}) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(3) > span:nth-child(2) > span:nth-child(1)').get()
        selector = scrapy.Selector(text=span_text)
        return selector.xpath('.//text()').get().strip()

    @staticmethod
    def remove_number_before_dot(text):
        return re.sub(r'^\d+\.\s', '', text)

```
Configurer le pipeline pour exporter en CSV : Dans le fichier `settings.py`, ajoutez ou modifiez la ligne suivante pour exporter les données en CSV:

```bash
FEED_FORMAT = 'csv'
FEED_URI = 'file:///MODIFIER_CETTE_VALEUR/imdb_films.csv'  # Chemin d'export à modifier
```

Exécutez le Spider : Exécutez le Spider en utilisant la commande suivante:

```bash
scrapy crawl imdb_spider
```
Là vous devriez avoir une erreur de type 403, c'est normal, c'est une protection anti-bot.

<img src="img/scrapy_error_403.png" alt="scrapy error 403">

## Contourner les 1er protections anti-bot

Une premiére étape de contournement consiste à utiliser un User-Agent de votre requête, tout en rajoutant un timer. Pour cela, ajoutez la ligne suivante dans le fichier `settings.py`:

```bash
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
DOWNLOAD_DELAY = 1.5  # Attendre 1,5 seconde entre chaque requête
```

Relancez le Spider : Relancez le Spider en utilisant la commande suivante:

```bash
scrapy crawl imdb_spider
```
Normalement, scrapy vous retourne un code 200 et vous devriez voir les informations extraites dans le fichier CSV.
<img src="img/scrapy_code_200.png" alt="scrapy code 200">

## Ressources

| Information                                                   | Lien                                                                               |
|---------------------------------------------------------------|------------------------------------------------------------------------------------|
| Warning : Web scraping et RGPD                                | https://www.plravocats.fr/blog/data-protection-rgpd/warning-web-scraping-et-rgpd   |
| scrapy                                                        | https://scrapy.org/             |
| Web Scraping with Python: Data Extraction from the Modern Web | https://www.oreilly.com/library/view/web-scraping-with/9781098145347/              |
| Architecture d’une protection anti-bot (Fabien Vauchelles)    | https://www.youtube.com/watch?v=bW17uUSG5TI                                        |

## Étape suivante

- [Étape 10](step_10.md)
