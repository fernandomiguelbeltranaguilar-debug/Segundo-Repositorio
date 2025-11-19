import tkinter as tk
from tkinter import messagebox

def dolar():
    try:
        cantidad = float(entry_cantidad.get())
        dolar = cantidad / 18.45
        etiqueta_resultado.config(text=f"DOLAR: ${dolar: .2f}")
        
    except ValueError:
        messagebox.showerror("Error","Ingresa una cantidad valida")



def euros():
    try:
        cantidad = float(entry_cantidad.get())
        euros = cantidad / 21.14
        etiqueta_resultado.config(text=f"EURO: ${euros: .2f}")

    except ValueError:
        messagebox.showerror("Error","Ingresa una cantidad valida")


def libras():
    try:
        cantidad = float(entry_cantidad.get())
        libras = cantidad / 24.63
        etiqueta_resultado.config(text=f"LIBRAS: ${libras: .2f}")

    except ValueError:
        messagebox.showerror("Error","Ingresa una cantidad valida")


def yenes():
    try:
        cantidad = float(entry_cantidad.get())
        yenes = cantidad / 0.12
        etiqueta_resultado.config(text=f"YENES: ${yenes: .2f}")

    except ValueError:
        messagebox.showerror("Error","Ingresa una cantidad valida")


#Creacion de la ventana 
ventana = tk.Tk()
ventana.title ("Tipo de cambio")
ventana.geometry("400x250")
ventana.resizable(False, False)

#etiqueta para que indique lo que tiene que escribir el usuario
etiqueta_cantidad = tk.Label(ventana, text="Ingresa la cantidad:")
etiqueta_cantidad.pack(pady=10)

#Crea una ventana para que el usuario ingresa la cantidad
entry_cantidad = tk.Entry(ventana, justify="center")
entry_cantidad.pack()

#Creacion de botones de accion 

btn_dolares = tk.Button(
    ventana,
    text="Calcular cantidad de dolares",
    command=dolar,
    bg="yellow"
)
btn_dolares.pack(pady=5)

btn_euros = tk.Button(
    ventana,
    text="Calcula la cantidad de euros",
    command=euros,
    bg="yellow"
)
btn_euros.pack(pady=5)

btn_libras = tk.Button(
    ventana,
    text="Calcular cantidad de libras",
    command=libras
)
btn_libras.pack(pady=5)

btn_yenes = tk.Button(
    ventana,
    text="Calcula la cantidad de yenes ",
    command=yenes
)
btn_yenes.pack(pady=5)

etiqueta_resultado = tk.Label(
    ventana,
    text="",
    font=("Arial", 12, "bold")
)
etiqueta_resultado.pack(pady=15)


ventana.mainloop()


