# def mi_generador():
#     x = 1
#     yield x

#     x += 1
#     yield x

#     x += 1
#     yield x


# g = mi_generador()

# print(next(g))
# print(next(g))
# print(next(g))


# def mi_generador():
#     generador = 1
#     while generador > 0:
#         yield generador
#         generador += 1


# g = mi_generador()
# print(next(g))
# print(next(g))

# def secuncia():
#     num = 7
#     while True:
#         yield num
#         num += 7


# g = secuncia()

# print(next(g))
# print(next(g))

def quitar_vidas():
    vida = 3
    while vida > 0:
        yield f"Te {'queda' if vida == 1 else 'quedan'} {vida} {'vida' if vida == 1 else 'vidas'}"
        vida -= 1
    yield "Game Over"


g = quitar_vidas()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

