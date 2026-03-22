import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# FUNCIONES

def agregar_evento():
    fecha = calendario.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    # Insertar en el TreeView
    tabla.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)


def eliminar_evento():
    seleccionado = tabla.selection()

    if not seleccionado:
        messagebox.showwarning("Advertencia", "Selecciona un evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Deseas eliminar el evento?")

    if confirmar:
        for item in seleccionado:
            tabla.delete(item)

def salir():
    root.quit()

# VENTANA PRINCIPAL

root = tk.Tk()
root.title("Agenda Personal")
root.geometry("700x500")

# FRAME: LISTA DE EVENTOS 

frame_lista = tk.Frame(root, bd=2, relief="groove")
frame_lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

titulo_lista = tk.Label(frame_lista, text="Eventos Programados")
titulo_lista.pack()

# Scroll
scroll = ttk.Scrollbar(frame_lista)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

# TreeView
tabla = ttk.Treeview(frame_lista, yscrollcommand=scroll.set)

tabla['columns'] = ("Fecha", "Hora", "Descripcion")

tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Fecha", anchor=tk.CENTER, width=100)
tabla.column("Hora", anchor=tk.CENTER, width=100)
tabla.column("Descripcion", anchor=tk.W, width=300)

tabla.heading("#0", text="")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Hora", text="Hora")
tabla.heading("Descripcion", text="Descripción")

tabla.pack(fill=tk.BOTH, expand=True)

scroll.config(command=tabla.yview)

#  FRAME: ENTRADA DE DATOS

frame_entrada = tk.Frame(root, bd=2, relief="groove")
frame_entrada.pack(padx=10, pady=5, fill=tk.X)

tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)

calendario = DateEntry(frame_entrada)
calendario.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)

entrada_hora = tk.Entry(frame_entrada)
entrada_hora.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)

entrada_descripcion = tk.Entry(frame_entrada, width=40)
entrada_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# FRAME: BOTONES 

frame_botones = tk.Frame(root, bd=2, relief="groove")
frame_botones.pack(padx=10, pady=10, fill=tk.X)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.pack(side=tk.LEFT, padx=10, pady=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.pack(side=tk.LEFT, padx=10, pady=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.pack(side=tk.RIGHT, padx=10, pady=5)

#EJECUCIÓN

root.mainloop()