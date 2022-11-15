# En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que
# contenga un botón de reinicio para que deje todo como al principio.
# Al principio no tiene que haber una opción seleccionada.
import tkinter as tk
from tkinter import ttk

window = tk.Tk()


def reset(event):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Radiobutton):
            seleccionado.set(None)


seleccionado = tk.IntVar()
r1 = tk.Radiobutton(window, text='Si', value=1, variable=seleccionado)
r1.grid(column=0, row=1, padx=5, pady=5)

r2 = ttk.Radiobutton(window, text='No', value=2, variable=seleccionado)
r2.grid(column=0, row=2, padx=5, pady=5)

r1 = ttk.Radiobutton(window, text='Quizás', value=3, variable=seleccionado)
r1.grid(column=0, row=3, padx=5, pady=5)

bt_reset = ttk.Button(window, text='Reset')
bt_reset.bind('<Button-1>', reset)
bt_reset.grid(column=0, row=4, pady=5, padx=5)
window.mainloop()
