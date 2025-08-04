import re

# texto = "si necesitas ayuda llama al (658) -598-9977 las 24 horas al servicio de ayuda online"

# patron = 'ayuda'

# busqueda = re.search(patron, texto)
# busqueda = re.findall(patron, texto)

# print(busqueda)
# print(len(busqueda))
# # print(busqueda.span())
# # print(busqueda.start())
# # print(busqueda.end())

# texto = "si necesitas ayuda llama al (658) -598-9977 las 24 horas al servicio de ayuda online"

# patron = 'ayuda'

# # busqueda = re.findall(patron, texto)

# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())

texto = 'llama al 564-525-6588 ya mismo'

# patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'
# utilizamos re.compile y los parentesis para que luego en el print group (1) salga el resultado de esa posicion
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

print(resultado)
print(resultado.group())
print(resultado.group(1))


# clave = input("clave: ")
# patron = r'\D{1}\w{7}'

# chequear = re.search(patron, clave)

# print(chequear)

texto2 = "No atendemos los lunes por la tarde"

buscar = re.search(r'lunes|martes', texto2)
print(buscar)

# Ejercicio 1 udemy


def verificar_email(email):
    # clave = input("tu correo: ")
    patron = r'^[\w\.-]+@[\w\.-]+\.com(\.\w+)?$'

    if re.match(patron, email):
        print("ok,correo correcto")
    else:
        print("la direccion es incorrecta")


verificar_email("matias@gmail.com.ar")

# ejercicio 2 udemy


def verificar_saludo(frase):
    patron = r'^Hola'

    if re.match(patron, frase):
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo("Hola soy matias")
verificar_saludo("soy matias")

# ejercio 3 udemy


def verificar_cp(cp):
    patron = r'[\w{2}]+[\d{4}]'

    if re.match(patron, cp):
        print("Ok")
    else:
        print("El codigo postal ingresado no es correcto")


verificar_cp("AB1234")

# ejercicio 1 hecho por fede


# def verificar_email(email):
#     patron = r'@\w+\.com'
#     verificar = re.search(patron, email)
#     if verificar:
#         print("Ok")
#     else:
#         print("La dirección de email es incorrecta")
