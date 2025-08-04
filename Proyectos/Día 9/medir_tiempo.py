import timeit


def prueb_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

# comprobacion segun time
# inicio = time.time()
# prueb_for(1000000)
# final = time.time()
# print(final - inicio)


# incio = time.time()
# prueba_while(1000000)
# final = time.time()
# print(final - inicio)

declaracion = """
prueb_for(10)
"""

mi_setup = """
def prueb_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

"""
on = timeit.timeit(declaracion, mi_setup, number=1000000)

print(on)


declaracion2 = """
prueba_while(10)
"""

mi_setup2 = """
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

"""

on2 = timeit.timeit(declaracion2, mi_setup2, number=1000000)
print(on2)
