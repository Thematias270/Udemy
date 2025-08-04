archivo = open(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/prueba.txt', 'w')

# archivo.write('Soy el nuevo texto')

# archivo.writelines(['hola','mundo','aqui','estoy'])

lista = ['hola', 'mundo', 'aqui', 'estoy']

for l in lista:
    archivo.writelines(l + '\n')


archivo = open(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/prueba.txt', 'a')

archivo.write('bienvenido')
archivo.close()
