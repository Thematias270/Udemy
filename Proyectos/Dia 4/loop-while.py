# monedas = 5

# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas = monedas - 1
# else:
#     print("No tienes mas monedas")

# respuesta = 's'

# while respuesta == 's':
#     respuesta = input("Quieres seguir? (s/n) ")
# else:
#     print("Gracias")

# respuesta = 's'

# while respuesta == 's':
#     pass

# print("hola")

# nombre = input("Dime tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         break
#     print(letra)

# nombre = input("Dime tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         continue
#     print(letra)

# numero = 50
# while numero >= 0:
#     if numero % 5 == 0:
#         print(numero)
#     numero = numero - 1

lista_numeros = [4, 5, 8, 7, 6, 9, 8, 2, 4,
                 5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]
for lista in lista_numeros:
    if lista < 0:
        break
    print(lista)
