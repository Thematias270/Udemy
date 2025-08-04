from random import *


intentos = 6
palabras = ['panadero', 'dinosaurio', 'batman', 'nebulosa', 'lluvia', 'girasol',
            'mariposa', 'caleidoscopio', 'esternocleidomastoideo', 'serenata', 'gisela', 'agustina']
palabra_aleatoria = choice(palabras)
letras_correctas = []
letras_incorrectas = []
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabra):
    palabra_elegida = choice(lista_palabra)
    letras_unicas = len(set(palabra_elegida))

    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida = ''
    valida = False
    abedecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abedecedario and len(letra_elegida) == 1:
            valida = True
        else:
            print('No ingresaste una letra valida')

    return letra_elegida


def mostrar_tablero(palabra_elegida):

    lista_oculta = []

    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')

    print(' '.join(lista_oculta))


def chequear(letra_elegida, palabra_oculta, vidas, coincidencias):

    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Papi,ya ingresaste esa letra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias


def perder():
    print('Te quedaste sin vidas')
    print('La palabra oculta era ' + palabra)

    return True


def ganar(palabra_descubierta):
    mostrar_tablero(palabra_descubierta)
    print('Felicidades!! \nHas encontrado la palabra!!')

    return True


palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()

    intentos, terminado, aciertos = chequear(
        letra, palabra, intentos, aciertos)

    juego_terminado = terminado
