# Universidad Estatal Amazonica
# William Delgado

class Producto:
    # Atributos
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = str(id_producto).strip()
        self.__nombre = str(nombre).strip()
        self.__cantidad = int(cantidad)
        self.__precio = float(precio)

    # Getters
    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def set_id(self, nuevo_id):
        self.__id = str(nuevo_id).strip()

    def set_nombre(self, nuevo_nombre):
        self.__nombre = str(nuevo_nombre).strip()

    def set_cantidad(self, nueva_cantidad):
        self.__cantidad = int(nueva_cantidad)

    def set_precio(self, nuevo_precio):
        self.__precio = float(nuevo_precio)

    def __str__(self):
        return (f"ID: {self.__id} | Nombre: {self.__nombre} | "
                f"Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}")


class Inventario:
    # Atributos
    def __init__(self):
        self.productos = []  # lista de objetos Producto

    # buscar por ID 
    def __indice_por_id(self, id_producto):
        id_producto = str(id_producto).strip()
        for i, prod in enumerate(self.productos):
            if prod.get_id() == id_producto:
                return i
        return None

    # nuevo producto
    def agregar_producto(self, producto):
        if self.__indice_por_id(producto.get_id()) is not None:
            print(" Error: Ya existe un producto con ese ID.")
            return False
        self.productos.append(producto)
        print(" Producto agregado correctamente.")
        return True

    # Eliminar producto por ID.
    def eliminar_producto(self, id_producto):
        idx = self.__indice_por_id(id_producto)
        if idx is None:
            print(" Error: Producto no encontrado.")
            return False
        eliminado = self.productos.pop(idx)
        print(f" Producto eliminado: {eliminado.get_nombre()} (ID {eliminado.get_id()})")
        return True

    # Actualizar cantidad o precio de un producto por ID.
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        idx = self.__indice_por_id(id_producto)
        if idx is None:
            print(" Error: Producto no encontrado.")
            return False

        prod = self.productos[idx]
        if cantidad is not None:
            prod.set_cantidad(cantidad)
        if precio is not None:
            prod.set_precio(precio)

        print(" Producto actualizado correctamente.")
        print(" ", prod)
        return True

    # Buscar producto(s) por nombre
    def buscar_por_nombre(self, texto):
        texto = str(texto).strip().lower()
        encontrados = []

        for prod in self.productos:
            if texto in prod.get_nombre().lower():
                encontrados.append(prod)

        if not encontrados:
            print(" No se encontraron productos con ese nombre.")
        else:
            print(f" Resultados encontrados ({len(encontrados)}):")
            for p in encontrados:
                print(" ", p)

        return encontrados

    # Mostrar todos los productos en el inventario.
    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
            return

        print("\n INVENTARIO ACTUAL")
        print("-" * 50)
        for prod in self.productos:
            print(prod)
        print("-" * 50)

# Interfaz de Usuario

def leer_int(msg, permitir_vacio=False):
    while True:
        dato = input(msg).strip()
        if permitir_vacio and dato == "":
            return None
        try:
            return int(dato)
        except ValueError:
            print(" Debe ingresar un número entero.")

def leer_float(msg, permitir_vacio=False):
    while True:
        dato = input(msg).strip()
        if permitir_vacio and dato == "":
            return None
        try:
            return float(dato)
        except ValueError:
            print(" Debe ingresar un número (ej: 12.5).")

def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto (cantidad / precio) por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Agregar Producto ---")
            id_producto = input("ID del producto (único): ").strip()
            nombre = input("Nombre del producto: ").strip()
            cantidad = leer_int("Cantidad: ")
            precio = leer_float("Precio: ")

            p = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(p)

        elif opcion == "2":
            print("\n--- Eliminar Producto ---")
            id_producto = input("Ingrese el ID a eliminar: ").strip()
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            print("\n--- Actualizar Producto ---")
            id_producto = input("Ingrese el ID a actualizar: ").strip()
            print("Deje en blanco lo que NO quiera cambiar.")
            cantidad = leer_int("Nueva cantidad: ", permitir_vacio=True)
            precio = leer_float("Nuevo precio: ", permitir_vacio=True)

            if cantidad is None and precio is None:
                print("⚠️ No ingresó cambios. No se actualizó nada.")
            else:
                inventario.actualizar_producto(id_producto, cantidad=cantidad, precio=precio)

        elif opcion == "4":
            print("\n--- Buscar Producto ---")
            texto = input("Ingrese nombre o parte del nombre: ").strip()
            inventario.buscar_por_nombre(texto)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema...")
            break

        else:
            print(" Opción inválida. Intente otra vez.")


if __name__ == "__main__":
    menu()
