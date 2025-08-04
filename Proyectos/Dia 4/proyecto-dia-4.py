from random import *


nombre = input("Bienvenido al juego, por favor introduce tu nombre: ")
print(f"""Hola {
      nombre}, he estado pensando un número del 1 al 100...\n¿crees que puedes adivinarlo?""")

intentos = 0
numero_jugador = 0
numero = randint(1, 100)

while intentos < 8 and numero_jugador != numero:
    numero_jugador = int(input('Dime tu numero: '))

    if numero_jugador not in (range(1,101)):
        print("Debes ingresar un numero del 1 al 100")

    elif numero_jugador < numero:
        print("El numero debe de ser mas alto")
        # print(f"te quedan {intentos} intentos")
    elif numero_jugador > numero:
        print("te pasaste debes de elegir un numero mas chico")
        # print(f"te quedan {intentos} intentos")

    intentos += 1

if numero_jugador == numero:
    print(f"""Felicidades {nombre} adivinaste el numero, el numero era {
          numero} y te a tomado {intentos} intentos para descubrilo""")
else:
    print(f"""lo siento, {nombre} te quedaste sin intentos. El numero era {
          numero} y te a tomado {intentos} intentos para descubrilo""")
