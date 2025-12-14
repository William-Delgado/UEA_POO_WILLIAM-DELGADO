# ==========================
# William Delgado
# UEA
# PROGRAMACIÓN TRADICIONAL
# Promedio semanal del clima
# ==========================
# El programa se organiza usando funciones.
# No se usan clases ni objetos y los datos se manejan con listas y variables.

def ingresar_temperaturas():
    """
    Función ingresa 7 temperaturas
    Devuelve una lista con las temperaturas ingresadas.
    """
    temperaturas = []  # Lista vacía para guardar las temperaturas de la semana

    # Bucle para la temperatura de cada uno de los 7 días
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)  # Guarda la temperatura en la lista

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Función que recibe una lista de temperaturas y calcula el promedio.
        """
    return sum(temperaturas) / len(temperaturas)


# -------- PROGRAMA PRINCIPAL --------
# 1) PedE las temperaturas de la semana
temperaturas_semana = ingresar_temperaturas()

# 2) Se calcula el promedio semanal usando otra función
promedio = calcular_promedio(temperaturas_semana)

# 3) Mostramos resultados
print("\nTemperaturas ingresadas:", temperaturas_semana)
print("Promedio semanal (Tradicional):", promedio)
