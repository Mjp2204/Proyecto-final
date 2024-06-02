import pygame
import sys
from pygame.locals import *
from datetime import datetime
from PIL import Image, ImageTk, ImageFilter
import tkinter as tk
import customtkinter as CTk
from carrito import *


# Ruta de las imágenes
ruta_juego = 'C:/Users/lenovo/Dropbox/PP/FINAL/Imagenes/Fondo.jpg'
ruta_fondo = 'C:/Users/lenovo/Dropbox/PP/FINAL/Imagenes/MenuInicio20.jpg'
ruta_logo = 'C:/Users/lenovo/Dropbox/PP/FINAL/Imagenes/Logo.png'


root = tk.Tk()
root.title('Highway Rush')
root.geometry('800x920')

# Cargar la imagen de fondo
try:
    image = Image.open(ruta_fondo)
    background_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit(1)

# Crear un canvas para poner la imagen de fondo
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_image, anchor="nw")
canvas.image = background_image

# Cargar imagen de fondo
try:
    fondo_jugar = Image.open(ruta_juego)
    distorted_image = fondo_jugar.filter(ImageFilter.BLUR) 
    distorted_image_tk = ImageTk.PhotoImage(distorted_image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit(1)

# Cargar el logo
try:
    image = Image.open(ruta_logo)
    logo_image = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error al cargar la imagen: {e}")
    exit(1)

root.call('wm', 'iconphoto', root._w, logo_image)

def jugar():
    boton_jugar.place_forget()
    boton_salir.place_forget()
    # Mostrar los campos de entrada y botón en el canvas
    nombre_label.place(x=490, y=500)
    nombre_entry.place(x=490, y=540)
    boton_iniciar.place(x=490, y=580)


def iniciar_juego():
    nombre = nombre_entry.get()
    nombre_label.place_forget()
    nombre_entry.place_forget()
    boton_iniciar.place_forget()
    boton_salir.place_forget()

    if nombre:
        # Limpiar el canvas
        canvas.delete("all")
        try:
            fondo_jugar = Image.open(ruta_juego)
            distorted_image = fondo_jugar.filter(ImageFilter.BLUR) 
            distorted_image_tk = ImageTk.PhotoImage(distorted_image)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            return

        canvas.create_image(0, 0, image=distorted_image_tk, anchor="nw")
        canvas.image = distorted_image_tk  
        mensaje = canvas.create_text(400, 460, text=f"Bienvenido, {nombre}! El juego comienza ahora.", fill="black", font=("8-bit Arcade In", 30))

        root.after(5000, lambda: canvas.delete(mensaje))

    def cuenta_regresiva(contador):
        if contador > 0:
            canvas.delete("contador")
            texto_contador = canvas.create_text(400, 460, text=str(contador), fill="black", font=("8-bit Arcade In", 100), tag="contador")
            root.after(1000, lambda: cuenta_regresiva(contador - 1))
        else:
            canvas.delete("contador")
            texto_start = canvas.create_text(400, 460, text="START!", fill="black", font=("8-bit Arcade In", 110))

    root.after(5000, lambda: cuenta_regresiva(5))

def salir():
    root.quit()

VERDE_CLARO = "#399183"
nombre_label = tk.Label(root, text="Ingrese su nombre:", font=("8-bit Arcade In", 16))
nombre_entry = tk.Entry(root, font=("8-bit Arcade In", 16))
boton_iniciar = tk.Button(root, text="Iniciar juego", command=iniciar_juego, font=("8-bit Arcade In", 16), bd=3, fg="black", bg= VERDE_CLARO, width=14, height=2)

VERDE_CLARO = "#399183"
boton_jugar = tk.Button(text="JUGAR", command=jugar, font=("8-bit Arcade In", 16), bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_jugar.place(x=490, y=500)

VERDE_CLARO = "#399183"
boton_salir = tk.Button(text="SALIR", command=salir, font=("8-bit Arcade In", 16), bd=3, fg="black", bg=VERDE_CLARO, width=14, height=2)
boton_salir.place(x=490, y=560)


root.mainloop()

Clock = pygame.time.Clock()


userName = str
points = 0
date = str
speed = 5
first = True
fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Maneja otros eventos como el teclado

    # Actualiza el estado del carrito del usuario
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        carrito_usuario.actualizar('izquierda')
    if keys[pygame.K_RIGHT]:
        carrito_usuario.actualizar('derecha')
    if keys[pygame.K_UP]:
        carrito_usuario.actualizar('arriba')
    if keys[pygame.K_DOWN]:
        carrito_usuario.actualizar('abajo')

    # Dibuja el carrito del usuario en la pantalla
    # Asumiendo que 'pantalla' es la superficie donde dibujas tu juego en Pygame
    pantalla.fill((0, 0, 0))  # Rellena la pantalla con negro
    carrito_usuario.dibujar(pantalla)
    pygame.display.flip()
    Clock.tick(60) 