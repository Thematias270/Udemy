# lista = ['a', 'b', 'c']

# # for item in enumerate(lista):
# #     print(item)
# # for item in enumerate(range(1, 10)):
# #     print(item)

# mis_tuples = list(enumerate(lista))
# print(mis_tuples)

# lista_nombres = ["Marcos", "Laura", "Mónica", "Javier",
#                  "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# for indice, nombre in enumerate(lista_nombres):
#     print(f'{nombre} se encuentra en el índice {indice}')

# nombre = "Python"
# lista_indices = list(enumerate(nombre))
# print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier",
                 "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)
