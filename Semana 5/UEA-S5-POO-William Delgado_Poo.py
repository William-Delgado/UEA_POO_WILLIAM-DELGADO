#William Delgado
#UEA-POO
# Programa: Calculadora de tarifa de estacionamiento
# Este programa calcula el costo de estacionamiento según el tipo de vehículo
# y las horas utilizadas. También aplica un descuento si el usuario es cliente frecuente.

def calcular_tarifa_por_hora(tipo_vehiculo):
    """
    Retorna la tarifa por hora según el tipo de vehículo.
    """
    if tipo_vehiculo == "moto":
        return 0.75
    elif tipo_vehiculo == "auto":
        return 1.50
    elif tipo_vehiculo == "camioneta":
        return 2.00
    else:
        return 0.0

def main():
    # string: datos de texto
    nombre_cliente = input("Nombre del cliente: ")
    tipo_vehiculo = input("Tipo de vehículo (moto/auto/camioneta): ").strip().lower()
    # int: horas como número entero
    horas = int(input("Horas de estacionamiento (ej: 3): "))
    # boolean: cliente frecuente (sí/no)
    respuesta_frecuente = input("¿Eres cliente frecuente? (s/n): ").strip().lower()
    es_cliente_frecuente = (respuesta_frecuente == "s")
    # float: tarifa y costos
    tarifa_por_hora = calcular_tarifa_por_hora(tipo_vehiculo)
    # Validación simple
    datos_validos = (tarifa_por_hora > 0) and (horas > 0)
    if not datos_validos:
        print("\nError: tipo de vehículo inválido o horas incorrectas.")
    else:
        subtotal = tarifa_por_hora * horas
        # Descuento si es cliente frecuente
        descuento = 0.10  # 10%
        if es_cliente_frecuente:
            total = subtotal * (1 - descuento)
        else:
            total = subtotal
        print("\n--- RESUMEN ---")
        print(f"Cliente: {nombre_cliente}")
        print(f"Vehículo: {tipo_vehiculo}")
        print(f"Horas: {horas}")
        print(f"Tarifa por hora: ${tarifa_por_hora:.2f}")
        print(f"Cliente frecuente: {es_cliente_frecuente}")
        print(f"Total a pagar: ${total:.2f}")

if __name__ == "__main__":
    main()
