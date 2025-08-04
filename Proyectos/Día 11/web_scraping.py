import bs4
import requests


resultado = requests.get(
    'https://escueladirecta-blog.blogspot.com/2024/07/buscas-trabajo-y-no-has-certificado-en.html?m=1')

# print(resultado.text)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa)
# print(sopa.select('title'))
# print(sopa.select('title')[0].get_text())

# columna_derecha = sopa.select('.post-title-container')
# print(columna_derecha)

columna_derecha = sopa.select('.post-title-container')

for p in columna_derecha:
    print(p.get_text())
