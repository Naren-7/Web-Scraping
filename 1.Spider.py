# Definir estrutura de los items
from scrapy.item import Item, Field
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader



# Definimos una clase que construra nuestros futuros item
class Pregunta(Item):
    pregunta = Field()  # Field: Perimite agregarle atributos a los nuevos items
    id = Field()


class StackOverflowSpider(Spider):  # Spider: Analiza una sola pagin Web
    name = "MiPrimerSpider"
    start_urls = ["http://stackoverflow.com/questions/"]

    def parse(self, response): # Response: Estado de que devuelve la pagina web por ejemplo (error: 404)

        sel = Selector(response)  # Selector: Selecciona una etiqueta.

        # Definimos una variable pregunta, que almacenara la equita segun mi objectivo a buscar.
        preguntas = sel.xpath('//div[@id="questions"]/div')  # Podemos usar el metodo css para identificar la inforamarcion en la pagina web.

        # iterar sobre todas la preguntas
        for i, ele in enumerate(preguntas):

            # Cargar item en una variable que tendra la Clase Preguntas y el item.
            item = ItemLoader(Pregunta(), ele)

            # Buscar el texto de cada pregunta y definirlo en cada item
            item.add_xpath("pregunta", ".//h3/a/text()")

            # Insertar id en nuestro futuro item
            item.add_value("id", i)

            # Retorne un item por cada iteracion.
            yield item.load_item()
            
            
# Comando para ejecuatr este script
#  scrapy runspider Spider.py  -o stack.csv -t csv   
# -0 : Nombre de nuestro archivo donde se almacenara la data
# -t : Tipo de formato


