# lista = ['a', 'b', 'c', 'd']

# for letra in lista:
#     numero_letra = lista.index(letra) + 1
#     print(f"Letra: {numero_letra}: {letra}")

# lista = ["pablo", "laura", "fede", "luis", "julia"]

# for nombre in lista:
#     if nombre.startswith('l'):
#         print(nombre)
#     else:
#         print("nombre que NO comienza con L " + nombre)

# numeros = [1, 2, 3, 4, 5]
# mi_valor = 0

# for numero in numeros:
#     mi_valor = mi_valor + numero
#     print(mi_valor)

# palabra = "python"
# for letra in palabra:
#     print(letra)

# for objeto in [[1, 2], [3, 4], [5, 6]]: for para listas
#     print(objeto)
# dic = {"clave1": 'a', "clave2": 'b', "clave3": 'c'}

# for item in dic.items():
#     print(item)

# dic = {"clave1": 'a', "clave2": 'b', "clave3": 'c'}

# # for item in dic.values():
# #     print(item)

# lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2,
#                  6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
# suma_numeros = 0
# for numero in lista_numeros:
#     suma_numeros += numero
#     print(lista_numeros)

# lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2,
#                  6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
# suma_pares = 0
# suma_impares = 0
# for numero in lista_numeros:
#     if numero % 2 == 0:
#         suma_pares += numero
#     else:
#         suma_impares += numero

# print(f"suma de numeros pares {suma_pares}")
# print(f"suma de numeros impares {suma_impares}")

lista_numeros = [3, -2, 7, -5, 8, -1, 4, -6, 9, -3, -4, 2, -7, 5, 1]

suma_positivos = 0

suma_negativos = 0

for numero in lista_numeros:
    if numero > 0:
        suma_positivos += numero
    else:
        suma_negativos += numero
print(f"la suma de los numeros positivos es: {suma_positivos}")
print(f"la suma de los numeros negativos es: {suma_negativos}")
