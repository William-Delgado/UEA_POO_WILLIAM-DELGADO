import tkinter as tk
from tkinter import messagebox

# FUNCIONES #
def agregar_tarea():
    tarea = entrada.get().strip()
    if tarea == "":
        messagebox.showwarning("Advertencia", "Ingrese una tarea")
        return
    
    lista_tareas.insert(tk.END, tarea)
    entrada.delete(0, tk.END)

def marcar_completada():
    try:
        indice = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice)

        # Evita duplicar el check
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice)
            lista_tareas.insert(indice, "✔ " + tarea)
    except:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

def eliminar_tarea():
    try:
        indice = lista_tareas.curselection()[0]
        lista_tareas.delete(indice)
    except:
        messagebox.showwarning("Advertencia", "Seleccione una tarea")

# EVENTOS DE TECLADO #
def tecla_enter(event):
    agregar_tarea()

def tecla_mas(event):
    # Evita que funcione mientras escribes
    if root.focus_get() != entrada:
        marcar_completada()

def tecla_menos(event):
    # Evita que funcione mientras escribes
    if root.focus_get() != entrada:
        eliminar_tarea()

def tecla_escape(event):
    root.quit()

# INTERFAZ #
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Entrada
entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
lista_tareas.pack(pady=10)

# ATAJOS DE TECLADO #

root.bind("<Return>", tecla_enter)         # Enter
root.bind("+", tecla_mas)                 # +
root.bind("-", tecla_menos)               # -
root.bind("<KP_Add>", tecla_mas)          # + teclado numérico
root.bind("<KP_Subtract>", tecla_menos)   # - teclado numérico
root.bind("<Escape>", tecla_escape)       # Escape

# Foco inicial
entrada.focus_set()
root.mainloop()

