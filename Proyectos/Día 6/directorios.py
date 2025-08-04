import os

# ruta = os.getcwd()  # obtener el directorio actual


# cambia directorio
# ruta = os.chdir(r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 5')

# archivo = open('esto.txt')

# print(archivo.read())

# archivo.close()

# cracion de carpeta
# ruta = os.makedirs(
#     r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 6\nuevo')

# print(ruta)

# ruta del archivo
# ruta = r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 6\prueba.txt'
# # obtener el nombre del archivo
# elemento = os.path.basename(ruta)

# # elemento = os.path.dirname(ruta) # ruta del directorio

# # elemento = os.path.split(ruta)  # obtener ambos,nombre del archivo y directorio

# # imprimir el nombre
# print(elemento)

# eliminar directorio
eliminar = os.rmdir(
    r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 6\nuevo')
print(eliminar)
