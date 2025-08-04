class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("se ha eliminado el cd")


mi_cd = CD('Pink Floyd', "The Wall", 24)

print(len(mi_cd))

print(mi_cd)


class Libro:
    def __init__(self, autor, titulo, cant_paginas):
        self.autor = autor
        self.titulo = titulo
        self.cant_paginas = cant_paginas

    def __str__(self):
        return f'Titulo: " {self.titulo} ", escrito por {self.autor} '

    def __len__(self):
        return self.cant_paginas


libro1 = Libro("Stephen King", "it", 1032)

print(libro1)
print(len(libro1))
