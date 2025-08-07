from gui.formulario_cachipun import creacion_juego
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Cachipún")

# Tamaño de la ventana
ancho_ventana = 810
alto_ventana = 500

imagen_original = Image.open("gui/static/img/fondo.png")
fondo = ImageTk.PhotoImage(imagen_original.resize((810, 500)))


# Obtener el tamaño de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()




# Crear un Label con la imagen
label_fondo = tk.Label(root, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

def redimensionar_fondo(event):
    global fondo_tk, imagen_original, label_fondo
    nuevo_ancho = event.width
    nuevo_alto = event.height

    # Redimensionar la imagen original
    imagen_redim = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)
    fondo_tk = ImageTk.PhotoImage(imagen_redim)

    # Actualizar la etiqueta
    label_fondo.config(image=fondo_tk)
    label_fondo.image = fondo_tk  # mantener referencia


# Calcular posición para centrar
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)

# Aplicar tamaño y posición centrada
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Enlazar evento de cambio de tamaño a la función
root.bind("<Configure>", redimensionar_fondo)


# Llamamos a la funcion creacion de juego para mostrar los 
creacion_juego(root)



# Mostrar ventana
root.mainloop()