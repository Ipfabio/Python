#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe
# de contener una lista de elementos seleccionables, también debe de tener un label con el
# texto que queráis.

import tkinter as tk
from tkinter import ttk

my_w = tk.Tk()  # Parent window
my_w.geometry("415x300")  # width and hight of the window


def my_reset():
    for widget in my_w.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, 'end')
        if isinstance(widget, ttk.Combobox):
            widget.delete(0, 'end')
        if isinstance(widget, tk.Text):
            widget.delete('1.0', 'end')
        if isinstance(widget, tk.Checkbutton):
            widget.deselect()


l1 = tk.Label(my_w, text='Nombre', font=28)
l1.grid(row=0, column=0, padx=10, pady=10)

e1 = tk.Entry(my_w, font=28)
e1.grid(row=0, column=1, padx=10, pady=10)

l2 = tk.Label(my_w, text='Apellido', font=28)
l2.grid(row=1, column=0, padx=10, pady=10)

e2 = tk.Entry(my_w, font=28)
e2.grid(row=1, column=1, padx=10, pady=10)

months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
cb1 = ttk.Combobox(my_w, values=months, width=7)
cb1.grid(row=2, column=1, padx=10, pady=10)

t1 = tk.Text(my_w, height=3, bg='grey', width=20)
t1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

ck1 = tk.Checkbutton(my_w, text='Terminos y condiciones', font=18)
ck1.grid(row=4, column=0, padx=10)

ck2 = tk.Checkbutton(my_w, text='Subscribirse a noticias', font=18)
ck2.grid(row=4, column=1, padx=10)

b1 = tk.Button(my_w, text='Enviar', font=22)
b1.grid(row=6, column=0, padx=10, pady=5)

r_v = tk.IntVar()
r1 = tk.Radiobutton(my_w, text='Opcion 1', value=1, font=18, variable=r_v)
r1.grid(row=5, column=0, pady=5, padx=5)

r2 = tk.Radiobutton(my_w, text='Opcion 2', value=2, font=18, variable=r_v)
r2.grid(row=5, column=1, pady=5, padx=5)

b2 = tk.Button(my_w, text='Reinicio', font=22, bg='red',fg='white', command=lambda: my_reset())
b2.grid(row=6, column=1, padx=10, pady=5)
my_w.mainloop()
