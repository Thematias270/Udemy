class vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")


class oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")


vaca1 = vaca('aurora')
oveja1 = oveja('nube')

# vaca1.hablar()
# oveja1.hablar()

# animales = [vaca1, oveja1]

# for animal in animales:
#     animal.hablar()


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
