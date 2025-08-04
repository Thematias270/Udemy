from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque

# numeros = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4]
# print(Counter(numeros))

serie = Counter([1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4])
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))


mi_dic = {'uno': 'verde', 'dos': 'azul', 'tres': 'rojo'}
print(mi_dic['tres'])

mi_dic = defaultdict(lambda: 'nada')
mi_dic['uno'] = 'verde'
print(mi_dic['dod'])

persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])

ariel = persona('ariel', 1.76, 79)
print(ariel.altura)

# ejercicio udemy 1
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)

print(contador)

# ejercicio udemy 2

mi_diccionario = {'edad': '44'}

mi_diccionario = defaultdict(lambda: 'Valor no hallado')

mi_diccionario['edad'] = 44
print(mi_diccionario['edad'])

# ejercicio udemy 3

lista_ciudades = deque(
    ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print(lista_ciudades)
