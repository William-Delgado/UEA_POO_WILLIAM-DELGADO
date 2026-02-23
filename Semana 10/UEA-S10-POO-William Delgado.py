import os

class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    # CARGAR INVENTARIO DESDE ARCHIVO
    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    try:
                        codigo, nombre, cantidad, precio = linea.strip().split(",")
                        self.productos[codigo] = Producto(
                            codigo,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )
                    except ValueError:
                        print(" Línea con formato incorrecto ignorada.")
        except FileNotFoundError:
            print(" Archivo no encontrado. Se creará uno nuevo.")
            self.guardar_en_archivo()
        except PermissionError:
            print(" Error: No tienes permisos para leer el archivo.")

    # GUARDAR INVENTARIO EN ARCHIVO
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for producto in self.productos.values():
                    f.write(str(producto) + "\n")
        except PermissionError:
            print(" Error: No tienes permisos para escribir en el archivo.")

    # AÑADIR PRODUCTO
    def agregar_producto(self, codigo, nombre, cantidad, precio):
        if codigo in self.productos:
            print(" El producto ya existe.")
        else:
            self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
            self.guardar_en_archivo()
            print(" Producto añadido y guardado correctamente.")

    # ACTUALIZAR PRODUCTO
    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo in self.productos:
            if cantidad is not None:
                self.productos[codigo].cantidad = cantidad
            if precio is not None:
                self.productos[codigo].precio = precio
            self.guardar_en_archivo()
            print(" Producto actualizado correctamente.")
        else:
            print(" Producto no encontrado.")

    # ELIMINAR PRODUCTO
    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_en_archivo()
            print(" Producto eliminado correctamente.")
        else:
            print(" Producto no encontrado.")

    # MOSTRAR INVENTARIO
    def mostrar_inventario(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for producto in self.productos.values():
                print(f"Código: {producto.codigo} | "
                      f"Nombre: {producto.nombre} | "
                      f"Cantidad: {producto.cantidad} | "
                      f"Precio: ${producto.precio}")
            print("--------------------------")


# INTERFAZ DE USUARIO
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                codigo = input("Código: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(codigo, nombre, cantidad, precio)

            elif opcion == "2":
                codigo = input("Código del producto a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(codigo, cantidad, precio)

            elif opcion == "3":
                codigo = input("Código del producto a eliminar: ")
                inventario.eliminar_producto(codigo)

            elif opcion == "4":
                inventario.mostrar_inventario()

            elif opcion == "5":
                print("👋 Saliendo del sistema...")
                break

            else:
                print(" Opción inválida.")

        except ValueError:
            print(" Error: Debe ingresar valores numéricos válidos.")
        except Exception as e:
            print(f" Error inesperado: {e}")


# Ejecutar programa
if __name__ == "__main__":
    menu()