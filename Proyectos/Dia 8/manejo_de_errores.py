# def suma():
#     n1 = int(input("numero1: "))
#     n2 = int(input("numero2: "))
#     print(n1 + n2)
#     print("gracias por sumar")


# try:
#     suma()
# except:
#     print("Algo no ha salido bien")
# else:
#     print("hiciste todo godines")
# finally:
#     print("Eso fue todo")


# logica try

# try:
#     # codigo que queremos probar
# except:
#     # codigo a ejecutar si no hay error
# finally:
#     # codigo que se va a ejecutar de todos modos


# otra forma de hacerlo es asi

# def pedir_numero():
#     while True:
#         try:
#             numero = int(input("Dame un numero: "))
#         except:
#             print("Ese no es un numero")
#         else:
#             print(f"Ingresaste el numero {numero}")
#             break

#     print("Gracias")


# pedir_numero()


def suma(num1, num2):
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("Error inesperado")
    except TypeError:
        return "El segundo argumento no debe ser cero"


suma(num1=2, num2=0)
