archivo = open(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/prueba.txt', 'w')

archivo.write('Nuevo texto')

# print(archivo)

archivo.close()

archivo = open(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/prueba.txt', 'r')

contenido = archivo.read()

print(contenido)

archivo.close()
