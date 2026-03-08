# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos que no cambiarán
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"Título: {self.info[0]}, Autor: {self.info[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} - ID: {self.id_usuario}"

    def listar_libros(self):
        if not self.libros_prestados:
            print("No tiene libros prestados.")
        else:
            print("Libros prestados:")
            for libro in self.libros_prestados:
                print(libro)

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario
        self.usuarios = {}
        self.ids_usuarios = set()  # Conjunto para IDs

    # Añadir libro
    def agregar_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente.")

    # Quitar libro
    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print("Usuario registrado correctamente.")
        else:
            print("El ID de usuario ya existe.")

    # Dar de baja usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)

        if libro and usuario:
            if libro.disponible:
                usuario.libros_prestados.append(libro)
                libro.disponible = False
                print("Libro prestado con éxito.")
            else:
                print("El libro no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        usuario = self.usuarios.get(id_usuario)

        if usuario:
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    libro.disponible = True
                    print("Libro devuelto correctamente.")
                    return
            print("El usuario no tiene este libro.")
        else:
            print("Usuario no encontrado.")

    # Buscar libros
    def buscar_libro(self, criterio):
        encontrados = []
        for libro in self.libros.values():
            if (criterio.lower() in libro.info[0].lower() or
                criterio.lower() in libro.info[1].lower() or
                criterio.lower() in libro.categoria.lower()):
                encontrados.append(libro)

        if encontrados:
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros.")

# Ejemplo de uso del sistema

biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("Don Quijote", "Miguel de Cervantes", "Clásico", "222")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Carlos Pérez", "U01")
usuario2 = Usuario("Ana López", "U02")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", "U01")

# Listar libros prestados
usuario1.listar_libros()

# Devolver libro
biblioteca.devolver_libro("111", "U01")

# Buscar libro
print("\nBúsqueda:")
biblioteca.buscar_libro("Don")