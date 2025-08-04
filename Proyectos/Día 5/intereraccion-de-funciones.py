# from random import *

# # lista inicial

# palitos = ['-', '--', '---', '----']

# # mezclar palitos


# def mezclar(lista):
#     shuffle(lista)
#     return lista

# # pedirle intento


# def probar_suerte():
#     intento = ''

#     while intento not in ['1', '2', '3', '4']:
#         intento = input('elige un numero del 1 al 4: ')

#     return int(intento)
# # comprobar intento
# def chequear_intento(lista, intento):
#     if lista[intento - 1] == '-':
#         print('a lavar los platos pa')
#     else:
#         print('te salvaste')

#     print(f"te a tocado {lista[intento - 1]}")


# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)

# from random import *


# def lanzar_dados():

#     a = randint(1, 6)
#     b = randint(1, 6)
#     suma = a + b
#     return suma


# def evaluar_jugada(suma):
#     if suma < 6:
#         print(f"""La suma de tus dados es {suma}. Lamentable""")
#     elif 6 <= suma < 10:
#         print(f"""La suma de tus dados es {suma}. Tienes buenas chances""")
#     elif suma >= 10:
#         print(f"""La suma de tus dados es {
#               suma}. Parece una jugada ganadora""")


# suma_dados = lanzar_dados()
# evaluar_jugada(suma_dados)

# from random import *


# def lanzar_dados():

#     dado1 = randint(1, 6)
#     dado2 = randint(1, 6)
#     return dado1, dado2


# def evaluar_jugada(dado1, dado2):
#     suma = dado1 + dado2
#     if suma <= 6:
#         return (f"""La suma de tus dados es {suma}. Lamentable""")
#     elif 7 <= suma < 10:
#         return (f"""La suma de tus dados es {suma}. Tienes buenas chances""")
#     elif suma >= 10:
#         return (f"""La suma de tus dados es {
#             suma}. Parece una jugada ganadora""")


# dado1, dado2 = lanzar_dados()

# resultado = evaluar_jugada(dado1, dado2)

# print(resultado)

# def reducir_lista(lista_numeros):
#     lista_sin_duplicados = list(set(lista_numeros))

#     valor_maximo = max(lista_sin_duplicados)

#     return lista_sin_duplicados


# def promedio(lista_sin_duplicados):
#     if len(lista_sin_duplicados) == 0:
#         return 0
#     return sum(lista_sin_duplicados) / len(lista_sin_duplicados)


# lista_numeros = [1, 2, 15, 7, 2]

# lista_reducida = reducir_lista(lista_numeros)

# resultado = promedio(lista_reducida)

# print(lista_reducida)
# print(resultado)

# def filtrar_pares(lista_numeros):
#     lista_pares = []
#     for n in lista_numeros:
#         if n % 2 == 0:
#             lista_pares.append(n)
#     return lista_pares


# def calcular_suma(lista_pares):
#     return sum(lista_pares)


# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# lista_pares = filtrar_pares(lista_numeros)

# resultado = calcular_suma(lista_pares)

# print(f"Lista de números pares: {lista_pares}")
# print(f"Suma total: {resultado}")

# from functools import reduce


# def filtrar_impares(lista_numeros):
#     lista_impares = []
#     for n in lista_numeros:
#         if n % 2 != 0:
#             lista_impares.append(n)
#     return lista_impares


# def multiplicar(lista_impares):
#     if not lista_impares:
#         return 1
#     return reduce(lambda x, y: x*y, lista_impares)


# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# lista_impares = filtrar_impares(lista_numeros)

# resultado = multiplicar(lista_impares)

# print(lista_impares)
# print(resultado)

from random import *


def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    aleatorio = choice(moneda)
    return aleatorio


def probar_suerte(aleatorio, lista_numeros):
    if aleatorio == 'Cara':
        print('La lista se autodestruirá')
        return []
    elif aleatorio == 'Cruz':
        print('La lista fue salvada')
        return lista_numeros


lista_numeros = [1, 2, 3, 4, 5]

aleatorio = lanzar_moneda()
resultado = probar_suerte(aleatorio, lista_numeros)

print(aleatorio)
print(resultado)
