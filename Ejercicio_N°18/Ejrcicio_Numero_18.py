import tkinter as tk
import random

# Número secreto
secreto = random.randint(1, 10)
vidas = 6  # ahora tienes 6 intentos

# Ventana
ventana = tk.Tk()
ventana.title("Juego: Adivina el número")
ventana.geometry("500x300+450+200")
ventana.config(bg="Black")

# Título
titulo = tk.Label(ventana, text="Adivina el número")
titulo.config(fg="red", bg="black", font=("Arial", 16))
titulo.place(x=250, y=20, anchor="center")

# Etiqueta de mensajes
etiqueta = tk.Label(ventana)
etiqueta.config(fg="white", bg="black", font=("Arial", 14, "italic"))
etiqueta.place(x=250, y=100, anchor="center")

# Entrada
entrada = tk.Entry(ventana)
entrada.config(bg="black", fg="red", font=("Arial", 12))
entrada.place(x=250, y=150, anchor="center")

# Función del juego
def aplicartexto():
    global vidas  #declaramos como variable global vidas (para usarla aqui dentro)

    numero = int(entrada.get())  # obtenemos lo que escribe la persona

    if numero == secreto:
        etiqueta.config(text="¡Adivinaste el número! ")
    else:
        vidas -= 1
        if vidas == 0:
            etiqueta.config(text=f"¡Perdiste! Era {secreto}")
            boton.config(state="disabled")
        else:
            if numero > secreto:
                etiqueta.config(text=f"El número secreto es menor. Te quedan {vidas} intentos")
            else:
                etiqueta.config(text=f"El número secreto es mayor. Te quedan {vidas} intentos")

# Botón
boton = tk.Button(ventana, text="Probar", command=aplicartexto)
boton.place(x=250, y=220, anchor="center")

ventana.mainloop()
