"""
Nombre: William Delgado
Tarea: Clase, Objeto, Herencia, Encapsulación y Polimorfismo
"""
class Empleado:
    """
    Clase base: Empleado, contiene atributos comunes a cualquier empleado y métodos generales.
    """
    def __init__(self, nombre: str, salario_base: float):
        self.nombre = nombre
        self._salario_base = salario_base  # Atributo protegido

    def calcular_salario(self) -> float:
        return self._salario_base

    def mostrar_info(self) -> str:
        return f"Empleado: {self.nombre} | Salario: ${self.calcular_salario():.2f}"


#  HERENCIA....POLIMORFISMO
class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre: str, salario_base: float, bono_mensual: float):
        super().__init__(nombre, salario_base)
        self.bono_mensual = bono_mensual

    # Polimorfismo: sobrescritura
    def calcular_salario(self) -> float:
        return self._salario_base + self.bono_mensual

# HERENCIA ...... ENCAPSULACIÓN
class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre: str, pago_por_hora: float):
        super().__init__(nombre, salario_base=0)
        self.pago_por_hora = pago_por_hora
        self.__horas_trabajadas = 0  # Encapsulación: atributo privado

    # Getter
    def get_horas_trabajadas(self) -> int:
        return self.__horas_trabajadas

    # Setter
    def set_horas_trabajadas(self, horas: int) -> None:
        if horas < 0:
            print(" Error: las horas no pueden ser negativas.")
        else:
            self.__horas_trabajadas = horas

    # Polimorfismo: sobrescritura
    def calcular_salario(self) -> float:
        return self.pago_por_hora * self.__horas_trabajadas

    def mostrar_info(self) -> str:
        return (f"Empleado por horas: {self.nombre} | "
                f"Horas: {self.get_horas_trabajadas()} | "
                f"Salario: ${self.calcular_salario():.2f}")

# FUNCIÓN QUE DEMUESTRA POLIMORFISMO
def imprimir_nomina(lista_empleados: list) -> None:

    if not lista_empleados:
        print("\n No hay empleados registrados.\n")
        return

    print("\n========== NÓMINA DE EMPLEADOS ==========")
    total = 0.0
    for emp in lista_empleados:
        print(emp.mostrar_info())
        total += emp.calcular_salario()

    print("----------------------------------------")
    print(f"Total a pagar: ${total:.2f}")
    print("========================================\n")

def leer_float(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje).strip())
            return valor
        except ValueError:
            print(" Entrada inválida. Ingresa un número (ej: 120.5).")

def leer_int(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje).strip())
            return valor
        except ValueError:
            print(" Entrada inválida. Ingresa un entero (ej: 40).")


def leer_texto(mensaje: str) -> str:
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print(" No puede estar vacío.")


#  MENÚ PRINCIPAL
def menu():
    empleados = []

    while True:
        print("===== MENÚ =====")
        print("1) Agregar empleado (genérico)")
        print("2) Agregar empleado a tiempo completo")
        print("3) Agregar empleado por horas")
        print("4) Mostrar nómina")
        print("5) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            nombre = leer_texto("Nombre del empleado: ")
            salario = leer_float("Salario base: ")
            empleados.append(Empleado(nombre, salario))
            print(" Empleado genérico agregado.\n")

        elif opcion == "2":
            nombre = leer_texto("Nombre del empleado: ")
            salario = leer_float("Salario base: ")
            bono = leer_float("Bono mensual: ")
            empleados.append(EmpleadoTiempoCompleto(nombre, salario, bono))
            print(" Empleado a tiempo completo agregado.\n")

        elif opcion == "3":
            nombre = leer_texto("Nombre del empleado: ")
            pago_hora = leer_float("Pago por hora: ")
            horas = leer_int("Horas trabajadas: ")

            emp = EmpleadoPorHoras(nombre, pago_hora)
            emp.set_horas_trabajadas(horas)  # Encapsulación: se asigna por setter
            empleados.append(emp)
            print(" Empleado por horas agregado.\n")

        elif opcion == "4":
            imprimir_nomina(empleados)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.\n")


#  EJECUCIÓN
if __name__ == "__main__":
    menu()
