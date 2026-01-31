import os
import sys
import subprocess


class Dashboard:
    def __init__(self):
        # Ruta donde está este archivo (probablemente Semana 8)
        here = os.path.dirname(os.path.abspath(__file__))

        # Si estoy dentro de una carpeta tipo "Semana X", subo al proyecto (POO)
        # Ej: .../POO/Semana 8 -> .../POO
        parent = os.path.dirname(here)

        # Si en el padre existen carpetas "Semana ...", uso el padre como base
        if self._tiene_semanas(parent):
            self.ruta_base = parent
        else:
            # Si no, uso donde está el archivo
            self.ruta_base = here

    def _tiene_semanas(self, ruta):
        try:
            for f in os.scandir(ruta):
                if f.is_dir() and f.name.lower().startswith("semana"):
                    return True
            return False
        except FileNotFoundError:
            return False

    def ejecutar(self):
        while True:
            carpetas = self.obtener_carpetas_principales()

            print("\n=== DASHBOARD - PROGRAMACIÓN ORIENTADA A OBJETOS ===")
            print(f"Ruta base: {self.ruta_base}\n")

            if not carpetas:
                print("No se encontraron carpetas (Semana X) en la ruta base.")
                print("0 - Salir")
                op = input("Opción: ").strip()
                if op == "0":
                    return
                continue

            for i, carpeta in enumerate(carpetas, start=1):
                print(f"{i} - {carpeta}")
            print("0 - Salir")

            opcion = input("Seleccione una carpeta (número o nombre): ").strip()

            if opcion == "0":
                print("Saliendo del Dashboard...")
                return

            carpeta_elegida = self.interpretar_opcion_carpeta(opcion, carpetas)
            if carpeta_elegida is None:
                print("Opción no válida.")
                continue

            ruta_carpeta = os.path.join(self.ruta_base, carpeta_elegida)
            self.menu_scripts(ruta_carpeta)

    def obtener_carpetas_principales(self):
        ignorar = {".git", ".idea", ".venv", "venv", "__pycache__"}
        carpetas = []
        for f in os.scandir(self.ruta_base):
            if f.is_dir() and f.name not in ignorar and not f.name.startswith("."):
                # Priorizamos semanas y ejemplos
                if f.name.lower().startswith("semana") or "poo" in f.name.lower():
                    carpetas.append(f.name)

        # Ordena: Semana 3, Semana 5, Semana 6...
        carpetas.sort(key=lambda x: x.lower())
        return carpetas

    def interpretar_opcion_carpeta(self, opcion, carpetas):
        # Si es número
        if opcion.isdigit():
            idx = int(opcion) - 1
            if 0 <= idx < len(carpetas):
                return carpetas[idx]
            return None

        # Si es nombre (ej: "Semana 3")
        opcion_norm = opcion.strip().lower()
        for c in carpetas:
            if c.lower() == opcion_norm:
                return c

        return None

    def menu_scripts(self, ruta_carpeta):
        while True:
            scripts = self.obtener_scripts(ruta_carpeta)

            print(f"\n--- Scripts en: {os.path.basename(ruta_carpeta)} ---")
            if not scripts:
                print("No hay scripts Python aquí.")
                print("0 - Regresar")
                op = input("Opción: ").strip()
                if op == "0":
                    return
                continue

            for i, script in enumerate(scripts, start=1):
                print(f"{i} - {script}")
            print("0 - Regresar")

            opcion = input("Seleccione un script (número o 0): ").strip()

            if opcion == "0":
                return

            if not opcion.isdigit():
                print("Opción no válida.")
                continue

            idx = int(opcion) - 1
            if not (0 <= idx < len(scripts)):
                print("Opción no válida.")
                continue

            script_seleccionado = scripts[idx]
            ruta_script = os.path.join(ruta_carpeta, script_seleccionado)

            self.mostrar_codigo(ruta_script)

            ejecutar = input("¿Desea ejecutar el script? (1 = Sí, 0 = No): ").strip()
            if ejecutar == "1":
                self.ejecutar_script(ruta_script)

            input("\nPresione Enter para continuar...")

    def obtener_scripts(self, ruta):
        return sorted([
            f.name for f in os.scandir(ruta)
            if f.is_file() and f.name.endswith(".py")
        ])

    def mostrar_codigo(self, ruta_script):
        print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
        try:
            with open(ruta_script, "r", encoding="utf-8") as archivo:
                print(archivo.read())
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def ejecutar_script(self, ruta_script):
        try:
            subprocess.Popen([sys.executable, ruta_script])
            print("Script ejecutándose...")
        except Exception as e:
            print(f"Error al ejecutar el script: {e}")


if __name__ == "__main__":
    Dashboard().ejecutar()
