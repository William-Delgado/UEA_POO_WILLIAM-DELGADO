"""
Nombre: William Delgado
Tema: Uso de Constructores y Destructores con Entrada de Datos

El programa permite registrar usuarios que se conectan a un servicio simulado.
Se utilizan constructores (__init__) para inicializar objetos y destructores (__del__)
para liberar recursos cuando los objetos dejan de existir.
"""

import gc
from datetime import datetime


class Conexion:
    """
    Simula una conexión a un servicio.
    """

    def __init__(self, servicio):
        # Constructor: se ejecuta al crear el objeto
        self.servicio = servicio
        self.activa = True
        print(f"[CONSTRUCTOR] Conexión establecida con el servicio: {self.servicio}")

    def enviar(self, mensaje):
        if not self.activa:
            print("No se puede enviar el mensaje. Conexión cerrada.")
            return
        print(f"[ENVÍO] {mensaje}")

    def cerrar(self):
        if self.activa:
            self.activa = False
            print(f"[CIERRE] Conexión cerrada con el servicio: {self.servicio}")

    def __del__(self):
        # Destructor: se ejecuta cuando el objeto es destruido
        if self.activa:
            print("[DESTRUCTOR] Cerrando conexión automáticamente...")
            self.cerrar()


class Usuario:
    """
    Representa a un usuario del sistema.
    """

    def __init__(self, nombre, servicio):
        # Constructor del usuario
        self.nombre = nombre
        self.conexion = Conexion(servicio)
        print(f"[CONSTRUCTOR] Usuario creado: {self.nombre}")

    def enviar_mensaje(self, texto):
        hora = datetime.now().strftime("%H:%M:%S")
        mensaje = f"{hora} | {self.nombre}: {texto}"
        self.conexion.enviar(mensaje)

    def cerrar_sesion(self):
        print(f"{self.nombre} está cerrando sesión...")
        self.conexion.cerrar()

    def __del__(self):
        print(f"[DESTRUCTOR] Usuario eliminado: {self.nombre}")


def main():
    print("===== SISTEMA DE REGISTRO =====\n")

    nombre = input("Ingrese su nombre: ")
    servicio = input("Ingrese el nombre del servicio: ")

    usuario = Usuario(nombre, servicio)

    while True:
        print("\n1. Enviar mensaje")
        print("2. Cerrar sesión")
        print("3. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            texto = input("Escriba el mensaje: ")
            usuario.enviar_mensaje(texto)

        elif opcion == "2":
            usuario.cerrar_sesion()

        elif opcion == "3":
            print("Saliendo del programa...")
            del usuario
            gc.collect()   # Forzamos recolección para ver __del__
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
