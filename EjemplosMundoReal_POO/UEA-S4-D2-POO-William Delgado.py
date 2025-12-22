class Estudiante:
    # Caso del mundo real: un estudiante con nombre y nota

    def __init__(self, nombre, nota=0):
        self.nombre = nombre
        self.nota = nota

    def cambiar_nota(self, nueva_nota):
        # Actualiza la nota del estudiante
        if 0 <= nueva_nota <= 10:
            self.nota = nueva_nota
        else:
            print("Nota inválida. Debe estar entre 0 y 10.")

    def aprueba(self):
        # Retorna True si aprueba, False si reprueba
        return self.nota >= 7

    def mostrar_info(self):
        estado = "Aprueba" if self.aprueba() else "Reprueba"
        print(f"Nombre: {self.nombre} | Nota: {self.nota} | Estado: {estado}")


# ---- Prueba del programa ----
alumno = Estudiante("Carlos", 6)
alumno.mostrar_info()

alumno.cambiar_nota(8)
alumno.mostrar_info()
