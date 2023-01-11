# Importamos las siguientes librerías:
#  - Item y Field: nos permiten crear estructuras para almacenar la información que obtendremos de la página web
#  - CrawlSpider y Rule: nos permiten crear un "araña" que navegará por la página web siguiendo un conjunto de reglas
#  - ItemLoader: nos permite cargar los datos en los Items que creamos
#  - LinkExtractor: nos permite buscar enlaces en la página web y seguirlos
#  - MapCompose: nos permite aplicar varias funciones a una misma entrada

from scrapy.item import Item, Field
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor 
from scrapy.loader.processors import MapCompose

# Creamos una clase para nuestro Item
class TechItems(Item):
    # Creamos dos campos para nuestro Item: dispositivo y precio
    dispositivo = Field()
    precio = Field()

# Creamos una clase para nuestro Spider
class JumboCrawler(CrawlSpider):
    # Le damos un nombre al Spider
    name = "MiPrimerCrawlspider"
    
    # Indicamos la URL donde empezará a buscar la información
    start_urls = ["https://www.tiendasjumbo.co/tecnologia/"]
    
    # Indicamos el o los dominios permitidos para el Spider
    allowed_domains = ["tiendasjumbo.co"]
    
    # Creamos una lista de reglas para el Spider
    rules = (        
        # Regla para moverse horizontalmente por la página web
        Rule(LinkExtractor(allow = r"page=" )),        
        
        # Regla para moverse verticalmente por la página web y aplicar una función a los items que cumplan con la condición
        Rule(LinkExtractor(allow = r"/p" ), callback = "parse_item")
    )
    
    # Definimos la función que se aplicará a los items que cumplan con la regla anterior
    def parse_item(self, response):
        # Definimos una función que elimina las comillas simples y dobles de un texto
        def remove_quotes(text):
            return text.replace("'", "").replace('"', "").replace('$', "")
    
        # Creamos un objeto ItemLoader.
        item = ItemLoader(TechItems(), response)
        
        # Añadimos el valor del campo "dispositivo" al Item
        item.add_xpath(
            field_name = "dispositivo",
            xpath = '//span[@class="vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--quickview "]/text()[normalize-space()][1]',
            input_processor = MapCompose(remove_quotes) )
        
        # Añadimos el valor del campo "precio" al Item
        item.add_xpath(
            field_name = "precio",
            xpath = "//*[@id='items-price']/div/div/text()[normalize-space()][1]", # normalize-space(): en XPath se utiliza para eliminar los espacios en blanco al principio y al final de una cadena, y para reemplazar cualquier secuencia de caracteres de espacio en blanco con un único carácter de espacio.
            input_processor = MapCompose(remove_quotes) )
        
        # Obtiene el Item cargado y lo devuelve.
        yield item.load_item()

