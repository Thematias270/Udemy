# """Crea una función llamada devolver_distintos() que reciba 3
# integers como parámetros.
# Si la suma de los 3 numeros es mayor a 15, va a devolver el
# número mayor.
# Si la suma de los 3 numeros es menor a 10, va a devolver el
# número menor.
# Si la suma de los 3 números es un valor entre 10 y 15
# (incluidos) va a devolver el número de valorintermedio."""


# def devolver_distintos(num1, num2, num3):
#     total = num1 + num2 + num3

#     mayor = max(num1, num2, num3)
#     menor = min(num1, num2, num3)

#     intermedio = total - mayor - menor

#     if total > 15:
#         return mayor
#     elif total < 10:
#         return menor
#     else:
#         return intermedio


# # Devolverá el menor, ya que la suma es menor a 10
# print(devolver_distintos(5, 3, 2))
# # Devolverá el intermedio, ya que la suma está entre 10 y 15
# print(devolver_distintos(6, 5, 4))
# # Devolverá el mayor, ya que la suma es mayor a 15
# print(devolver_distintos(10, 4, 3))

# """Escribe una función (puedes ponerle cualquier nombre que
# quieras) que reciba cualquier palabra como parámetro, y que
# devuelva todas sus letras únicas (sin repetir) pero en orden
# alfabético.
# Por ejemplo si al invocar esta función pasamos la palabra
# "entretenido"
# , debería devolver ['d','e','i','n','o','r',t']"""


# def ordenar(palabra):
#     caracteres = list(palabra)

#     caracteres_unicos = set(caracteres)  # set elimina duplicados

#     # sorted ordena,se puede usar para int
#     caracteres_ordenas = sorted(caracteres_unicos)

#     palabra_ordenada = ''.join(caracteres_ordenas)  # unir

#     return palabra_ordenada


# print(ordenar('programacion'))
# print(ordenar('examen'))

# """Escribe una función que requiera una cantidad indefinida de
# argumentos. Lo que hará esta función es devolver True si en
# algún momento se ha ingresado al numero cero repetido dos
# veces consecutivas.
# Por ejemplo:
# (5,6,1,0,0,9,3,5) >>> True
# (6,0,5,1,0,3,0,1) >>> False"""


# def encontrar(*args):
#     for n in range(len(args)-1):
#         if args[n] == 0 and args[n+1] == 0:
#             return True
#         else:
#             return False


# print(encontrar(5, 3, 4, 5, 6))
# print(encontrar(0, 0, 1, 2, 3, 4))


# def contar_negativos(*args):
#     contar = 0
#     for n in args:
#         if n < 0:
#             contar += 1
#     return contar


# print(contar_negativos(5, -3, 4, -2, 0, -1, -10, -43))

# """Escribe una función llamada contar_primos() que requiera un
# solo argumento numérico.
# Esta función va a mostrar en pantalla todos los números
# primos existentes en el rango que va desde cero hasta ese
# número incluido, y va a devolver la cantidad de números
# primos que encontró.
# Aclaración, por convención el 0 y el 1 no se consideran primos."""


def contar_primos(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0

    while iteracion <= numero:

        for n in range(3, iteracion, 2):

            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)


print(contar_primos(50))
