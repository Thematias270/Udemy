# from pathib import Path
from pathlib import PureWindowsPath

# carpeta = Path(
#     r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 6\prueba.txt')
# print(carpeta.read_text())
# print(carpeta.name) # extrae el nombre del archivo,prueba.txt
# print(carpeta.suffix) # extrae el tipo de archivo osea .txt
# print(carpeta.stem) # extrae solo el nombre del archivo,osea prueba

# carpeta = Path(
#     r'C:\Users\spide\OneDrive\Documentos\Udemy\Proyectos\Día 6\prueba.txt')

# if not carpeta.exists():
#     print('Este archivo no existe')
# else:
#     print('Joya,existe')

# usar PureWindowsPath

ruta = PureWindowsPath(
    'C:/Users/spide/OneDrive/Documentos/Udemy/Proyectos/Día 6/esto.txt')

# Imprimir la ruta
print(ruta)
