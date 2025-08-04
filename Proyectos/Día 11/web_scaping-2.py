import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# imagenes = sopa.select('.course-box-image')

# for i in imagenes:
#     print(i)

imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_curso_1 = requests.get(imagenes)
print(imagen_curso_1.content)

m = open('mi_imagen.jpg', 'wb')
m.write(imagen_curso_1.content)
m.close()
