import tkinter as tk
import random

ventana = tk.Tk()
ventana.title("Juego: Adivina el número")
ventana.geometry("500x400+450+200")
ventana.config(bg="Black")

# Título
titulo = tk.Label(ventana, text="Cifrado cesar")
titulo.config(fg="red", bg="black", font=("Arial", 18, "bold"))
titulo.place(x=250, y=20, anchor="center")

# Etiqueta de mensajes
etiqueta = tk.Label(ventana, text="Colocar mensaje a cifrar: ")
etiqueta.config(fg="white", bg="black", font=("Arial", 15, "italic"))
etiqueta.place(x=20, y=70)


# Etiqueta del numero
etiqueta = tk.Label(ventana, text="Colocar numero: ")
etiqueta.config(fg="white", bg="black", font=("Arial", 15, "italic"))
etiqueta.place(x=20, y=135)

#Mensaje ingresado
ingresado = tk.Label(ventana, text="mensaje ingresado")
ingresado.config(fg="red", bg="black", font=("Arial", 16))
ingresado.place(x=20, y=230)

# Mensaje cifrado
cifrados = tk.Label(ventana, text="mensaje cifrado")
cifrados.config(fg="red", bg="black", font=("Arial", 16))
cifrados.place(x=20, y=180)

# Entrada de mensaje
entrada = tk.Entry(ventana)
entrada.config(bg="black", fg="red", font=("Arial", 12))
entrada.place(x=255, y=70)

# Entrada de numero
entradaint = tk.Entry(ventana)
entradaint.config(bg="black", fg="red", font=("Arial", 12))
entradaint.place(x=180, y=140)

def cifradoCesar(texto, desplazamiento):
    
    resultado = ""
    for c in texto:
        
        if c.isalpha():
            
            base = ord('A') if c.isupper() else ord('a')
            resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            
        else:
            
            resultado += c
    return resultado

def cifrar():
    
    texto = entrada.get()
    
    try:
        numero = int(entradaint.get())
        
    except ValueError:
        
        ingresado.config(text=" El número debe ser un entero.")
        cifrados.config(text="")
        return

    mensaje_cifrado = cifradoCesar(texto, numero)
    mensaje_descifrado = cifradoCesar(mensaje_cifrado, -numero)

    cifrados.config(text=f"Mensaje cifrado: {mensaje_cifrado}")
    ingresado.config(text=f"Mensaje descifrado: {mensaje_descifrado}")
# Botón
boton = tk.Button(ventana, text="Probar", command=cifrar)
boton.place(x=250, y=320, anchor="center")

ventana.mainloop()