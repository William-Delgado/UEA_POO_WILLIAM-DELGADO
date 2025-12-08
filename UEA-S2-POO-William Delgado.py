
#     Clase base: Animal
class Animal:
    def __init__(self, nombre, especie, edad):
        # 2. ENCAPSULAMIENTO (Protección de los atributos)

        self._nombre = nombre
        self._especie = especie
        self._edad = edad

    # -------- MÉTODO DE ABSTRACCIÓN --------
    def descripcion(self):
        """Devuelve una descripción general del animal."""
        return f"{self._nombre} ({self._especie}), {self._edad} años"

    # -------- MÉTODOS DE ENCAPSULAMIENTO --------
    def get_edad(self):
        return self._edad

    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        if len(nuevo_nombre) > 1:
            self._nombre = nuevo_nombre

# 3. HERENCIA (Perro y Gato heredan de Animal)
# ---------------------------------------------------------
# Se reutilizan los atributos básicos: nombre, especie y edad.
# Se agregan atributos propios de cada tipo de animal:
#   - Perro: raza
#   - Gato: color
# Así se evita duplicar código y se mejora la organización.
# ---------------------------------------------------------
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, "Perro", edad)
        self.raza = raza

    # ---------------------------------------------
    # 4. POLIMORFISMO: redefinir descripcion()
    # ---------------------------------------------
    def descripcion(self):
        return (f"Perro: {self._nombre}, {self._edad} años - "
                f"Raza: {self.raza}")

    def ladrar(self):
        return "Guau guau!"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, "Gato", edad)
        self.color = color

    # Polimorfismo nuevamente aplicado
    def descripcion(self):
        return (f"Gato: {self._nombre}, {self._edad} años - "
                f"Color: {self.color}")

    def maullar(self):
        return "Miau!"


#     PROGRAMA PRINCIPAL (uso de las clases)

p1 = Perro("Max", 5, "Labrador")
g1 = Gato("Luna", 3, "Blanco")
a1 = Animal("Criatura", "Desconocida", 10)

# Polimorfismo en acción: mismo método, diferente resultado
print(a1.descripcion())
print(p1.descripcion())
print(g1.descripcion())

# Métodos propios de cada clase
print(p1.ladrar())
print(g1.maullar())

# Uso del encapsulamiento
p1.set_edad(6)
p1.set_nombre("Maxito")

print("Nuevo nombre:", p1.get_nombre())
print("Nueva edad:", p1.get_edad())
