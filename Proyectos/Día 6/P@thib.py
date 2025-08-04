from pathlib import Path

archivo = Path(
    r'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 5/esto.txt')

with archivo.open() as mi_archivo:
    print(mi_archivo.read())

# 1. Crear una ruta
# archivo = Path(r'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/esto.txt')

#  2. Leer el archivo usando 'with'
# with archivo.open(mode='r', encoding='utf-8') as mi_archivo:
#     contenido = mi_archivo.read()

# # 3. Imprimir el contenido
# print(contenido)
