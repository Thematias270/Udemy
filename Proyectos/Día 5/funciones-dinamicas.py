# def chequear_3_cifras(numero):
#     return numero in range(100, 1000)


# suma = 586 + 402

# resultado = chequear_3_cifras(suma)

# print(resultado)

# def chequear_3_cifras(lista):

#     lista_3_cifras = []

#     for n in lista:
#         if n in range(100, 1000):
#             lista_3_cifras.append(n)
#         else:
#             pass
#     return lista_3_cifras


# # resultado = chequear_3_cifras([55, 99, 6000])
# resultado = chequear_3_cifras([555, 95, 60])

# print(resultado)

# def todos_positivos(lista):
#     for n in lista:
#         if n < 0:
#             return False
#     return True


# lista_numeros = [10, 2, 4]

# resultado = todos_positivos(lista_numeros)
# print(resultado)

# def todos_positivos(lista):
#     mostrar_lista = []
#     for n in lista:
#         if n < 0:
#             mostrar_lista.append(n)
#             # return False
#         else:
#             pass
#     return mostrar_lista


# # lista_numeros = [10, 2, 4]

# # resultado = todos_positivos(lista_numeros)
# resultado = todos_positivos([-12, 4, 5])
# print(resultado)

# def suma_menores(lista):
#     suma = 0
#     for n in lista:
#         if 0 < n < 1000:
#             suma += n
#     return suma


# # lista_numeros = [150, 500, 1001, -50, 300]

# resultado = suma_menores([150, 500, 50, 10])

# print(resultado)

# def cantidad_pares(lista):
#     contador = 0
#     for n in lista:
#         if n % 2 == 0:
#             contador += 1
#     return contador

# lista_numeros = [2,4,7]

# resultado = cantidad_pares(lista_numeros)

# print(resultado)

# def maximo_lista(lista_numeros):

#     maximo = lista_numeros[0]

#     for n in lista_numeros:
#         if n > maximo:
#             maximo = n
#     return maximo


# lista_numeros = [12, 32, 56]

# resultado = maximo_lista(lista_numeros)

# print(resultado)

# def minimo_lista(lista):
#     minimo = lista[0]
#     for n in lista:
#         if n < minimo:
#             minimo = n
#     return minimo


# lista = [12, 4, 5, 6, 9]

# resultado = minimo_lista(lista)

# print(resultado)

def producto_lista(lista_numeros):
    producto = 1
    for n in lista_numeros:
        producto *= n

    return producto


lista_numeros = [2, 4, 6]

resultado = producto_lista(lista_numeros)

print(resultado)
