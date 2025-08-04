import bs4
import requests

# url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# for n in range(1, 11):
#     print(url_base.format(n))

# resultado = requests.get(url_base.format('1'))
# sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# libros = sopa.select('.product_pod')

# ejemplo = libros[0].select('a')[1]['title']
# print(ejemplo)
# toda la parte de arriba era el ejemplo antes del proyecto,en vez de borrar y hacer de nuevo
# lo dejo de ejemplo

# crear url sin numero de pagina gracias al {}
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 11):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            # guardar titulo en varible
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

# ver libros 4 o 5 estrellas en consola

for t in titulos_rating_alto:
    print(t)
