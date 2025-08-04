class Padre:
    def hablar(self):
        print("hola")


class Madre:
    def reir(self):
        print("ja ja ja")

    def hablar(self):
        print("que tal")


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()

print(Nieto.__mro__)
