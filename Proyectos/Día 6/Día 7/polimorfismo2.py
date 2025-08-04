"""Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len()."""

# palabra = "polimorfismo"
# lista = ["clases", "poo", "polimorfismo"]
# tupla = (1, 2, 3, 80)

# nuevo = [palabra, lista, tupla]

# for n in nuevo:
#     print(len(n))


"""Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden."""

#    class Mago():
#         def atacar(self):
#             print("Ataque mágico")

#     class Arquero():
#         def atacar(self):
#             print("Lanzamiento de flecha")

#     class Samurai():
#         def atacar(self):
#             print("Ataque con katana")

#     personajes = [Arquero, Mago, Samurai]

#     for n in personajes:
#         n.atacar(personajes)


"""Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate."""


# class Mago():
#     def defender(self):
#         print("Escudo mágico")


# class Arquero():
#     def defender(self):
#         print("Esconderse")


# class Samurai():
#     def defender(self):
#         print("Bloqueo")


# def personaje_defender(guerrero):
#     guerrero.defender()


# personajes = [Mago, Arquero, Samurai]

# for guerrero in personajes:
#     guerrero.defender(personajes)


# Encapsulamiento
class Persona:
    atributo_publico = "Mostrar"
    __atributo_privado = "Oculto"

    def __metodo_oculto(self):
        print("Este metodo esta oculto")
        self.__variable = 0

    def metodo_normal(self):
        self.__metodo_oculto()


alumno = Persona()

# alumno.__metodo_oculto()

alumno.metodo_normal()
