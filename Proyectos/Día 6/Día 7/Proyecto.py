class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0.0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def mostrar(self):
        return f'cuenta bancaria de "{self.nombre} {self.apellido}" numero de la cuenta {self.numero_cuenta} y su saldo es {self.balance} '

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Deposito Exitoso!! Nuevo saldo: ${self.balance:.2f}")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.balance:
                self.balance -= cantidad
                print(f"💸Retiro Exitoso!! Nuevo saldo: ${self.balance:.2f}")
            else:
                (f"❌ Saldo insuficiente para realizar el retiro.")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su numero de cuenta: ")
    return Cliente(nombre, apellido, numero_cuenta)


def inicio():
    cliente = crear_cliente()

    while True:
        print("\n" + "="*40)
        print("🏦 MENU PRINCIPAL - BANCO PYTHON 🏦")
        print("="*40)
        print("1️⃣ Depositar Dinero")
        print("2️⃣ Retirar Dinero")
        print("3️⃣ Mostrar Dinero")
        print("4️⃣ Salir")
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            monto = float(input("ingrese la cantidad a depositar: "))
            cliente.depositar(monto)
        elif opcion == "2":
            monto = float(input("Ingrese la cantidad a retirar: "))
            cliente.retirar(monto)
        elif opcion == "3":
            print(cliente.mostrar())
        elif opcion == "4":
            print("👋 Gracias por usar Banco Python!!!")
            break


inicio()
