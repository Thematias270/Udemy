mi_archivo = open(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/prueba.txt')

# contenido = mi_archivo.read()

# print(contenido)

# una_linea = mi_archivo.readline()
# print(una_linea.upper())

# una_linea = mi_archivo.readline()
# print(una_linea)

# una_linea = mi_archivo.readline()
# print(una_linea)

# for l in mi_archivo:
#     print("aqui dice: " + l)

todas = mi_archivo.readlines()  # asi se hace para listas

todas = todas.pop()#solo muestra la ultima linea

print(todas)

mi_archivo.close()
segunda = open('Prueba.txt')
lineas = segunda.readlines()
segunda_linea = lineas[1]
print(segunda_linea)