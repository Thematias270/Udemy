from pathlib import Path

base = Path.home()
guia = Path('barcelona', 'sagrada_familia.txt')
print(guia)
print(base)


"""Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py"""
"Curso Python"
"Día 6"
"practicas_path.py"


ruta = Path('Curso Python', 'Día 6', 'practicas_path.py')

relativa = ruta.relative_to(Path())

print(relativa)

"""Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py"""

"Curso Python"
"Día 6"
"practicas_path.py"


base = Path.home()

ruta = Path(base, 'Curso Python', 'Día 6', 'practicas_path.py')

print(ruta)
