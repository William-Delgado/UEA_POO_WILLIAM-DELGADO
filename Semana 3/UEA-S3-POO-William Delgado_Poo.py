# ==========================
# William Delgado
# UEA
# PROGRAMACIÓN POO
# Promedio semanal del clima
# ==========================
# El programa se organiza usando clases y objetos.
# Encapsulamiento: las temperaturas se guardan dentro del objeto.
# Herencia: usamos una clase base y una clase hija.

class ClimaBase:
    """
    La clase base almacena temperaturas y permite calcular promedios.
    Sirve como estructura para cualquier tipo de clima.
    """

    def __init__(self):
        # _temperaturas es un atributo (encapsulamiento)
        self._temperaturas = []

    def agregar_temperatura(self, temp):
        """
        agrega una temperatura a la lista interna del objeto.
        """
        self._temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Método que calcula el promedio de las temperaturas almacenadas.
        """
        if len(self._temperaturas) == 0:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(ClimaBase):
    """
    Clase hija que hereda de ClimaBase.
    """

    def ingresar_semana(self):
        """
        Solicita al usuario ingresar la temperatura de los 7 días.
        Usa el método heredado 'agregar_temperatura' para guardarlas.
        """
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.agregar_temperatura(temp)  # Método heredado de ClimaBase

    def mostrar_resultados(self):
        """
        Muestra las temperaturas guardadas y el promedio semanal calculado.
        Usa el método heredado 'calcular_promedio'.
        """
        print("\nTemperaturas ingresadas:", self._temperaturas)
        print("Promedio semanal (POO):", self.calcular_promedio())


# -------- PROGRAMA PRINCIPAL5--------
# 1) Creamos un objeto de la clase ClimaSemanal
clima = ClimaSemanal()

# 2) Ingresamos las temperaturas usando métodos del objeto
clima.ingresar_semana()

# 3) Mostramos resultados desde el mismo objeto
clima.mostrar_resultados()
