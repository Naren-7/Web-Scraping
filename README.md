# Web-Scraping

Este proyecto tiene como objetivo mostrar cómo utilizar las tecnologías Scrapy, Selenium y BeautifulSoup para realizar web scraping de manera eficiente y fácil.

## Requisitos previos
- Tener Python instalado en su sistema.
- Tener conocimientos básicos de Python y programación en general.

## Instalación

1. Instale las dependencias utilizando pip:

```bash
pip install scrapy selenium beautifulsoup4

```
2. Puedes usar un nuevo ambiente local con `Conda`, el archivo **[requeimientos.yml](https://github.com/Naren-7/Web-Scraping/blob/main/requerimient.yml)** está en el repositorio.
```
conda create --name mi_nuevo_entorno --file requerimient.yml
```
## Uso
Para utilizar este proyecto, siga los siguientes pasos:

1. Abra una terminal o línea de comandos.
2. Navegue hasta la carpeta del proyecto en su sistema.
3. Ejecute el siguiente comando para iniciar la extracción de datos:

```bash
scrapy runspider script_name.py -o file_name.csv -t csv --set CLOSESPIDER_ITEMCOUNT=number  

```
## Flags indispensable
- `-o`: Crear o escribe en un archivo.
- `-t`: Tipo de formato del archivo.
- `--set CLOSESPIDER_ITEMCOUNT=number`: Este parámetro establece un límite para el número de elementos a ser scraped.

## Advertencia
Algunos sitios web pueden prohíbir el scraping de sus contenidos. Asegúrese de leer y entender los términos y condiciones de un sitio web antes de utilizar este proyecto para extraer sus datos.
