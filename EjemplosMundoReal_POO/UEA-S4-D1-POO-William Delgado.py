class CuentaBancaria:
    # Caso del mundo real: una cuenta bancaria con saldo y operaciones básicas

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depósito: +${monto} | Nuevo saldo: ${self.saldo}")
        else:
            print("Monto inválido para depositar.")

    def retirar(self, monto):
        if monto <= 0:
            print("Monto inválido para retirar.")
        elif monto > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= monto
            print(f"Retiro: -${monto} | Nuevo saldo: ${self.saldo}")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: ${self.saldo}")
# ---- Prueba del programa (uso de la clase) ----
cuenta = CuentaBancaria("Ana", 100)
cuenta.mostrar_saldo()
cuenta.depositar(50)
cuenta.retirar(30)
cuenta.retirar(200)
