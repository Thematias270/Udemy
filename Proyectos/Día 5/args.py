def suma(*args):
    total = 0

    for n in args:
        total += n
    return total


print(suma(5, 6, 4, 5, 5,-1))

# def suma(*args):

#     return sum(args)


# print(suma(5, 6,4,5,5))

# def suma_cuadrados(*args):
#     return sum(args)


# print(suma_cuadrados(1, 2, 3, 5))


# def suma_cuadrados(*args):
#     suma = 0
#     for n in args:
#         suma += n ** 2
#     return suma


# print(suma_cuadrados(1, 4, 9))

# def suma_absolutos(*args):
#     total = 0

#     for n in args:
#         total += abs(n)
#     return total


# print(suma_absolutos(1, 2, 3, -4))
