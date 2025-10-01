import cv2
import os

# Ruta donde se guardarán las imágenes
ruta_dataset = "Proyectos/Dia 14/Empleados"

# Nombre del empleado
nombre = input("Ingrese el nombre del empleado: ")

# Crear carpeta si no existe
ruta_empleado = os.path.join(ruta_dataset, nombre)
os.makedirs(ruta_empleado, exist_ok=True)

# Captura desde celular con DroidCam
url_droidcam = "http://192.168.1.52:4747/video"
captura = cv2.VideoCapture(url_droidcam)

contador = 0
max_fotos = 3  # cantidad de imágenes por empleado

print("📸 Presione 'q' para salir antes de tiempo")

# Cargamos el detector de caras
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    exito, frame = captura.read()
    if not exito:
        print("❌ No se pudo conectar con la cámara de DroidCam. Revisá la URL y que la app esté abierta.")
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    caras = face_cascade.detectMultiScale(gris, 1.3, 5)

    for (x, y, w, h) in caras:
        rostro = frame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150))
        cv2.imwrite(f"{ruta_empleado}/{nombre}_{contador}.jpg", rostro)
        contador += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Captura de dataset", frame)

    if cv2.waitKey(1) & 0xFF == ord('q') or contador >= max_fotos:
        break

print(f"✅ Dataset generado: {contador} imágenes guardadas en {ruta_empleado}")
captura.release()
cv2.destroyAllWindows()
