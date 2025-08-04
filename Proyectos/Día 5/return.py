# def multiplicar(numero1, numero2):
#     total = numero1 * numero2
#     print(total)
#     return total

#     # return numero1 * numero2


# # print(multiplicar(5, 10))
# resultado = multiplicar(5, 10)

# print(resultado)

# def potencia(base, exponente):
#     return base ** exponente


# print(potencia(10, 9))

# def usd_a_eur(dolares):
#     euros = dolares * 0.9
#     return euros


# dolares = 55
# resultado = usd_a_eur(dolares)

# print(resultado)

def invertir_palabra(palabra):
    palabra_invertida = palabra.upper()[::-1]

    return palabra_invertida


palabra = 'Hola Mundo'

resultado = invertir_palabra(palabra)
print(resultado)
