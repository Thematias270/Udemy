texto = input("ingresa un texto: ").lower()

largo = len(texto)

primera_letra = texto[0]

ultima_letra = texto[-1]

texto_invertido = texto[::-1]

python = "python" in texto

dic = {True: "Sí", False: "No"}


print(f"El largo del texto es: {largo}")

print("Este es el texto en minuscula: " + texto)

print("Esta es tu primera letra ingresada: " + primera_letra)

print("Esta fue tu ultima letra ingresada: " + ultima_letra)

print(f"Asi seria el texto al reves: {texto_invertido}")

print(f"La palabra 'Python' {dic[python]} se encuentra en el texto")

letras = []

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se encontro la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Se encontro la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Se encontro la letra '{letras[2]}' repetida {cantidad_letras3} veces")
