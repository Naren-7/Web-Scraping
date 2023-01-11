# Importamos las siguientes librerías:
#  - Item y Field: nos permiten crear estructuras para almacenar la información que obtendremos de la página web
#  - CrawlSpider y Rule: nos permiten crear un "araña" que navegará por la página web siguiendo un conjunto de reglas
#  - ItemLoader: nos permite cargar los datos en los Items que creamos
#  - LinkExtractor: nos permite buscar enlaces en la página web y seguirlos
#  - MapCompose: nos permite aplicar varias funciones a una misma entrada.
#   - BeautifulSoup:  permite parsear y navegar fácilmente a través del contenido de un documento HTML o XML.

from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor 
from scrapy.loader.processors import MapCompose
from bs4 import BeautifulSoup


class LeMondeItem(Item):
    titulo = Field()
    contenido = Field()


class LeMondeCrawlSpider(CrawlSpider):
    name = 'LeMondeCrawle'
    allowed_domains = ['lemonde.fr']
    start_urls = ['https://www.lemonde.fr/euro-2020/']
    
    allow_patterns = [r'/sport/article/2021/07/12/euro-2021-', r'/planete/article/2021/07/10/euro-2021-', r'/sport/article/2021/07/12/']
    
    rules = (
        Rule(LinkExtractor(allow = r'euro-2020/\d+'), follow = True),  # \d+ : Numero digital
        Rule( 
            LinkExtractor(allow = r'/sport/article/2021/07/12/euro-2021-'), 
            callback = "parse_items", follow = True)   
        )
    
    def parse_items(self, response):
        item = ItemLoader(LeMondeItem(), response)
        item.add_xpath(field_name = "titulo", xpath = '//h1/text()')
        soup = BeautifulSoup(response.body)
        
        articule = soup.find("div", class_="article__content  old__article-content-single")        
        contenido = articule.text
        
        # agegar contenido
        item.add_value("contenido", contenido)
        
        yield item.load_item()