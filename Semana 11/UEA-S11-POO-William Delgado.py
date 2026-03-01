import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
    def get_id(self):
        return self.id_producto
    def get_nombre(self):
        return self.nombre
    def get_cantidad(self):
        return self.cantidad
    def get_precio(self):
        return self.precio
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
    def set_precio(self, precio):
        self.precio = precio
    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

class Inventario:
    def __init__(self):
        self.productos = {}
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print(" Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print(" Producto agregado correctamente.")
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(" Producto eliminado.")
        else:
            print(" Producto no encontrado.")
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print(" Producto actualizado.")
        else:
            print(" Producto no encontrado.")
    def buscar_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)
        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()} | {p.get_nombre()} | Cant: {p.get_cantidad()} | $ {p.get_precio()}")
        else:
            print(" No se encontraron productos.")
    def mostrar_todos(self):
        if not self.productos:
            print(" Inventario vacío.")
        else:
            print("\n INVENTARIO:")
            for p in self.productos.values():
                print(f"ID: {p.get_id()} | {p.get_nombre()} | Cant: {p.get_cantidad()} | $ {p.get_precio()}")
    def guardar_archivo(self, archivo="inventario.json"):
        with open(archivo, "w") as f:
            json.dump({id: prod.to_dict() for id, prod in self.productos.items()}, f, indent=4)
        print(" Inventario guardado en inventario.json")
    def cargar_archivo(self, archivo="inventario.json"):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                for id, prod in data.items():
                    self.productos[int(id)] = Producto(
                        prod["id"], prod["nombre"], prod["cantidad"], prod["precio"]
                    )
            print(" Inventario cargado.")
        except FileNotFoundError:
            print(" No existe archivo de inventario aún.")

def menu():
    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print(" Error: Datos inválidos.")
        elif opcion == "2":
            id_producto = int(input("ID a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == "3":
            id_producto = int(input("ID a actualizar: "))
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)
        elif opcion == "5":
            inventario.mostrar_todos()
        elif opcion == "6":
            inventario.guardar_archivo()
        elif opcion == "7":
            inventario.cargar_archivo()
        elif opcion == "8":
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()