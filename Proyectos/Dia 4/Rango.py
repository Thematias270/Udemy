# lista = [1, 2, 3, 4]

# for numero in range(1, 5, 3):
# for numero in range(1, 5, 3):
#     print(numero)

# lista = list(range(1, 101))

# print(lista)

# suma_cuadrados = 0

# for numero in range(1,16):
#     cuadrado = numero ** 2
#     suma_cuadrados += cuadrado


# print(suma_cuadrados)

# suma_impares = 0

# for numero in range(1, 21):
#     if numero % 2 != 0:
#         cubo = numero **3
#         suma_impares += cubo

# print(suma_impares)

# suma_total_pares = 0
# suma_total_impares = 0

# for numero in range(2, 51):
#     if numero % 2 == 0:
#         suma_total_pares += numero
#     else:
#         suma_total_impares += numero

# print(suma_total_pares)
# print(suma_total_impares)

# suma_multiplos = 0

# for numero in range(1, 101):
#     if numero % 3 == 0 or numero % 5 == 0:
#         suma_multiplos += numero
# print(suma_multiplos)

suma_multiplos = 0

for numero in range(1, 101):
    if numero % 6 == 0:
        suma_multiplos += numero
print(suma_multiplos)
