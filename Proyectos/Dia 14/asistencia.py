import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# 📌 Ruta del dataset
ruta = "Proyectos/Dia 14/Empleados"
nombres_empleados = []
lista_empleados_codificada = []

# Codificar todas las imágenes del dataset


def cargar_dataset(ruta):
    imagenes = []
    nombres = []

    for carpeta in os.listdir(ruta):
        ruta_empleado = os.path.join(ruta, carpeta)
        if os.path.isdir(ruta_empleado):
            for archivo in os.listdir(ruta_empleado):
                path = os.path.join(ruta_empleado, archivo)
                imagen = cv2.imread(path)
                if imagen is not None:
                    imagenes.append(imagen)
                    nombres.append(carpeta)
    return imagenes, nombres


def codificar(imagenes):
    lista_codificada = []
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codigos = fr.face_encodings(imagen)
        if len(codigos) > 0:
            lista_codificada.append(codigos[0])
    return lista_codificada


def registrar_ingresos(persona):
    fecha = datetime.now().strftime('%d/%m/%Y')
    hora = datetime.now().strftime('%H:%M:%S')

    with open('Proyectos/Dia 14/registro.csv', 'a+') as f:
        f.seek(0)
        lista_datos = f.readlines()
        registros = [linea.strip().split(',')
                     for linea in lista_datos if linea.strip()]

        ya_registrado = any(p[0] == persona and p[1] ==
                            fecha for p in registros)

        if not ya_registrado:
            f.write(f'{persona},{fecha},{hora}\n')
            print(f"✅ Registro guardado: {persona} - {fecha} {hora}")


ultimo_log = {}


def registrar_log(persona):
    ahora = datetime.now()
    fecha = ahora.strftime('%d/%m/%Y')
    hora = ahora.strftime('%H:%M:%S')

    if persona in ultimo_log:
        diferencia = (ahora - ultimo_log[persona]).total_seconds()
        if diferencia < 5:
            return

    with open('Proyectos/Dia 14/log.csv', 'a') as f:
        f.write(f'{persona},{fecha},{hora}\n')
        print(f"📒 Log: {persona} - {fecha} {hora}")

    ultimo_log[persona] = ahora


# 📌 Cargar y codificar dataset
imagenes, nombres_empleados = cargar_dataset(ruta)
lista_empleados_codificada = codificar(imagenes)
print("Empleados cargados:", set(nombres_empleados))

# 📌 Captura de cámara
# captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
captura = cv2.VideoCapture("http://192.168.1.52:4747/video")

print("🎥 Iniciando reconocimiento facial... (presiona Q para salir)")

while True:
    exito, imagen = captura.read()
    if not exito:
        print("No se ha podido tomar la captura")
        break

    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        nombre = "Desconocido"

        if len(distancias) > 0:
            indice_coincidencia = numpy.argmin(distancias)
            # umbral más tolerante gracias al dataset
            if distancias[indice_coincidencia] <= 0.5:
                nombre = nombres_empleados[indice_coincidencia]

        registrar_ingresos(nombre)
        registrar_log(nombre)

        y1, x2, y2, x1 = caraubic
        color = (0, 255, 0) if nombre != "Desconocido" else (0, 0, 255)
        cv2.rectangle(imagen, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
        cv2.putText(imagen, nombre, (x1 + 6, y2 - 6),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow('Reconocimiento Facial', imagen)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
