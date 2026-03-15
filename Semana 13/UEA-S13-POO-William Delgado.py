import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar_dato():
    dato = entrada.get()
    
    if dato != "":
        lista_datos.insert(tk.END, dato)  # Agrega el dato a la lista
        entrada.delete(0, tk.END)         # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese un dato.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI")
ventana.geometry("400x400")

# Título
titulo = tk.Label(ventana, text="Aplicación para Agregar Datos", font=("Arial", 14))
titulo.pack(pady=10)

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack()

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()