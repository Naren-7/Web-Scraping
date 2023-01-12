# Importamos las siguientes librerías:
#  - Item y Field: nos permiten crear estructuras para almacenar la información que obtendremos de la página web
#  - CrawlSpider y Rule: nos permiten crear un "araña" que navegará por la página web siguiendo un conjunto de reglas
#  - ItemLoader: nos permite cargar los datos en los Items que creamos
#  - LinkExtractor: nos permite buscar enlaces en la página web y seguirlos
#  - MapCompose: nos permite aplicar varias funciones a una misma entrada.
#   - BeautifulSoup:  permite parsear y navegar fácilmente a través del contenido de un documento HTML o XML.
#  - Selenium: Es un driver que  permite tener una interacción con uan pagina Web, podemos hacer scroll, click, extrar información, actua como si fuera una persona interactuando con una pagina.

# from scrapy.item import Item, Field
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.loader import ItemLoader
# from scrapy.linkextractors import LinkExtractor 
# from scrapy.loader.processors import MapCompose
# from bs4 import BeautifulSoup
from selenium import webdriver
import random
from time import sleep

# Instalar driver de Firefox con Arch Linux
# -  sudo pacman -S geckodriver   

# Definimos un navegador
options = webdriver.FirefoxOptions()

# se utiliza para deshabilitar las extensiones en Firefox al iniciar una sesión con Selenium. Al deshabilitar las extensiones, se garantiza que no interfieran con el comportamiento del navegador mientras se realizan pruebas automatizadas.
options.add_argument("--disable-extensions")

# Abrimo el navegador y le pasamos el dirver que controlara la pagina
driver = webdriver.Firefox(options=options, executable_path=r"/usr/bin/geckodriver")

# Obtenemos la pagina web.
driver.get("https://www.olx.com.co/motos_c379/")



# Definir variable que almacenar la posicion del boton que permite cargar los nuevos datos de la pagina.
boton = driver.find_element('xpath', '//button[@data-aut-id="btnLoadMore"]')

for _ in range(3):
    try:
        # ahora le daremos click al boton cuadno estemos en la pagina.
        boton.click()

        # Realizar un tiempo de espera para hacaer el click
        sleep(random.randint(8, 10))
        
        # volver a buscar el nuevo boton para luego hacerle click
        boton = driver.find_element('xpath', '//button[@data-aut-id="btnLoadMore"]')
    except: 
        break



# Todos los elementos dentro de una lista.
motos = driver.find_elements("xpath", '//li[@data-aut-id="itemBox"]')

for moto in motos:
    try:
        # Encontrar precio
        precio = moto.find_element("xpath", './/span[@data-aut-id="itemPrice"]').text
        print(precio)
    except:
        print("No se pudo encontrar el precio")
    
    try:
        # Encontrar descripcion
        descripcion = moto.find_element("xpath", './/span[@data-aut-id="itemTitle"]').text
        print(descripcion)
    except:
        print("No se pudo encontrar la descripcion")
        pass
