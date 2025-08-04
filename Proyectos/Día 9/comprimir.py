# import zipfile
import shutil

# cracion de un archivo comprimido
# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# guardar archivos al archivo comprido

# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')

# mi_zip.close()

# extracion del archivo comprimido

# zip_abierto = zipfile.ZipFile('Proyecto_Dia_9.zip', 'r')

# zip_abierto.extractall()

# carpeta_origen = 'C:\\Users\\spide\\OneDrive\\Documentos\\Udemy\\Proyectos\\Día 9\\Proyecto Día 9'

# archivo_destino = 'Proyecto_Dia_9'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Proyecto_Dia_9.zip',
                      'C:\\Users\\spide\\OneDrive\\Documentos\\Udemy\\Proyectos\\Día 9\\Proyecto Día 9', 'zip')
