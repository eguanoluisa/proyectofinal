import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

# funcion para quitar tag HTML
def RemoveHTMLTags(strr):
    # Print string after removing tags
   return re.compile(r'<[^>]+>').sub('', strr)


# URL del sitio web que deseas analizar
url = 'https://www.cep.org.ec/'
# Realizar una solicitud HTTP GET a la URL
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Analizar el contenido HTML de la página web
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraer el título de la página
    title = soup.title.string

    # Extraer la Serie y la Ddescripción de la página
    meta_serie_0 = RemoveHTMLTags(str(soup.findAll('h3', class_='elementor-image-box-title')[0]))
    meta_description_0 = RemoveHTMLTags(str(soup.findAll('p', class_='elementor-image-box-description')[0]))

    meta_serie_1 = RemoveHTMLTags(str(soup.findAll('h3', class_='elementor-image-box-title')[1]))
    meta_description_1= RemoveHTMLTags(str(soup.findAll('p', class_='elementor-image-box-description')[1]))

    meta_serie_2 = RemoveHTMLTags(str(soup.findAll('h3', class_='elementor-image-box-title')[2]))
    meta_description_2 = RemoveHTMLTags(str(soup.findAll('p', class_='elementor-image-box-description')[2]))

    meta_serie_3 = RemoveHTMLTags(str(soup.findAll('h3', class_='elementor-image-box-title')[3]))
    meta_description_3 = RemoveHTMLTags(str(soup.findAll('p', class_='elementor-image-box-description')[3]))

    # conectamos la base de datos Mysql
    # conexion = mysql.connector.connect(user="ceporgec_eddyguanoluisa", password="ZFS!&^JC}yjE", host="66.225.241.82",
    #                                   database="ceporgec_maestria_eddy", port="3306")
    conexion = mysql.connector.connect(user="root", password="", host="localhost", database = "maestria_ciberseguridad", port = "3306")

# ingresa datos a Mysql
    if conexion.is_connected():
        print("conexion exitosa")
        cursor = conexion.cursor()
        query = "INSERT INTO principal (titulo_pagina,serie,descripcion) VALUES ('" + title + "','" + meta_serie_0 + "','" + meta_description_0 + "')"
        cursor.execute(query)
        query = "INSERT INTO principal (titulo_pagina,serie,descripcion) VALUES ('" + title + "','" + meta_serie_1 + "','" + meta_description_1 + "')"
        cursor.execute(query)
        query = "INSERT INTO principal (titulo_pagina,serie,descripcion) VALUES ('" + title + "','" + meta_serie_2 + "','" + meta_description_2 + "')"
        cursor.execute(query)
        query = "INSERT INTO principal (titulo_pagina,serie,descripcion) VALUES ('" + title + "','" + meta_serie_3 + "','" + meta_description_3 + "')"
        cursor.execute(query)
        conexion.commit()

# FIN DEL PROGRAMA
    print("Se ha ingresado con exito los datos a la Base")
else:
    print("Error al acceder a la página. Código de estado:", response.status_code)