# def suma(**kwargs):
#     print(type(kwargs))


# suma(x=3, y=5, z=2)

# def suma(**kwargs):
#     total = 0
#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")
#         total += valor
#     return total


# print(suma(x=3, y=5, z=2))

# def prueba(num1, num2, *args, **kwargs):

#     print(f"el primer valor es {num1}")
#     print(f"el segundo valor es {num2}")

#     for arg in args:
#         print(f"arg = {arg}")

#     for clave, valor in kwargs.items():
#         print(f"{clave} = {valor}")


# # prueba(15, 50, 100, 200, 300, 400, x='uno', y='dos', z='tres')

# args = [100, 200, 300, 400]
# kwargs = {'x': 'uno', 'z': 'dos', 'y': 'tres'}

# prueba(15, 50, *args, **kwargs)

# def cantidad_atributos(**kwargs):
#     total = 0

#     for clave, valor in kwargs.items():
#         total += 1

#     return total


# print(cantidad_atributos(x=2, y=5, z=3, b=2))

# def lista_atributos(**kwargs):
#     return list(kwargs.values())


# print(lista_atributos(x='batman', z='robin'))

# def describir_persona(nombre, **kwargs):
#     print(f"Características de {nombre}")

#     for clave, valor in kwargs.items():
#         print(f'{clave} = {valor}')


# describir_persona('Matías', color_ojos='azules', color_pelo='rubio')



