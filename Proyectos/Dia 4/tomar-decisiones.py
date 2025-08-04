
# if 10 > 9:
#     print("Es correcto")
# else:
#     print("no es correcto")

# mascota = input("dime un animal: ")

# if mascota == "gato":
#     print("tienes un gato")
# elif mascota == "perro":
#     print("tienes un perro")
# elif mascota == "pez":
#     print("tienes un pez")
# else:
#     print("no que animal tienes")

# edad = int(input("dime tu edad: "))

# calificacion = int(input("dime tu calificacion: "))

# if edad < 18:
#     print("Eres menor de edad")
#     if calificacion >= 7:
#         print("Aprobado")
#     else:
#         print("Desaprobated")
# else:
#     print("Eres adulto")

# num1 = int(input("Ingresa un número: "))

# num2 = int(input("Ingresa otro número: "))

# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print(f"{num1} y {num2} son iguales")
# edad = 16
# tiene_licencia = False

# if edad > 18:
#     print("Puedes conducir")
# elif edad > 18 and tiene_licencia:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
# else:
#     print("No puedes conducir. Necesitas contar con una licencia")


edad = 16
tiene_licencia = False

# Verificar condiciones
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")

edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia:
    print("Puedes conducir")
elif edad < 18:
    print("No puedes conducir. Necesitas tener 18 años y contar con una licencia")
else:
    print("No puedes conducir. Necesitas contar con una licencia")
