class Pajaro:
    Alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print('pio, mi color es {}'.format(self.color),
              'mi especie es {}' .format(self.especie))

    def volar(self, metros):
        print(f"el pajaro a volado {metros} metros")

    def pintar_negro(self):
        self.color = 'negro'
        print(f"ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")
        cls.Alas = False
        print(Pajaro.Alas)

    @staticmethod
    def mirar():
        print("el pajaro mira")


piolin = Pajaro('amarillo', 'canario')

Pajaro.mirar()
piolin.piar()
piolin.pintar_negro()
piolin.poner_huevos(3)
piolin.volar(50)

"""
Práctica Métodos 1
Crea una clase Perro. Dicho perro debe poder ladrar.

Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!"."""


class Perro:
    def ladrar(self):
        print('Guau!')


choco = Perro()

choco.ladrar()

"""Práctica Métodos 2
Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo."""


class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")


merlin = Mago()
merlin.lanzar_hechizo()

"""Práctica Métodos 3
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"""

"La alarma ha sido pospuesta {cantidad_minutos} minutos"


class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
