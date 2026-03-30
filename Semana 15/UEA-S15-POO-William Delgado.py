import tkinter as tk
from tkinter import messagebox, ttk


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicación de Lista de Tareas")
        self.root.geometry("450x450")

        # Campo de entrada 
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.focus()

        # Evento: presionar ENTER
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botón añadir
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas
        self.tasks = ttk.Treeview(root, columns=('Tarea'), show='headings')
        self.tasks.heading('Tarea', text='Lista de Tareas')
        self.tasks.pack(fill=tk.BOTH, expand=True, pady=10)

        # Evento: doble clic para completar
        self.tasks.bind('<Double-1>', self.toggle_task_completion)

        # Botones 
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        self.complete_button = tk.Button(frame_buttons, text="Marcar como Completada",
                                         command=lambda: self.toggle_task_completion(complete=True))
        self.complete_button.grid(row=0, column=0, padx=5)

        self.uncomplete_button = tk.Button(frame_buttons, text="Desmarcar",
                                           command=lambda: self.toggle_task_completion(complete=False))
        self.uncomplete_button.grid(row=0, column=1, padx=5)

        self.delete_button = tk.Button(frame_buttons, text="Eliminar",
                                       command=self.delete_task)
        self.delete_button.grid(row=0, column=2, padx=5)

        # Evento: ESC para cerrar
        self.root.bind('<Escape>', lambda event: self.root.destroy())

    # FUNCIONES 

    def add_task(self):
        """Añade una nueva tarea a la lista"""
        task = self.task_entry.get().strip()

        if task:
            self.tasks.insert('', tk.END, values=(task,))
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Ingresa una tarea válida.")

    def toggle_task_completion(self, event=None, complete=True):
        """Marca o desmarca una tarea"""
        selected_item = self.tasks.selection()

        if not selected_item:
            messagebox.showinfo("Información", "Selecciona una tarea.")
            return

        if complete:
            self.tasks.item(selected_item, tags=('completed',))
            self.tasks.tag_configure('completed', background='lightgreen')
        else:
            self.tasks.item(selected_item, tags=('pending',))
            self.tasks.tag_configure('pending', background='white')

    def delete_task(self):
        """Elimina una tarea seleccionada"""
        selected_item = self.tasks.selection()

        if selected_item:
            self.tasks.delete(selected_item)
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

# EJECUCIÓN 
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()