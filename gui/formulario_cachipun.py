import random
import tkinter as tk
from tkinter import PhotoImage
import os
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from model.cachipun_modelo import guardar_partida, obtener_partidas, limpiar_tabla_cachipun

cachipun = ["piedra", "papel", "tijera"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Cargar imágenes después de inicializar root
ruta_piedra = os.path.join(BASE_DIR, 'static', 'img', 'piedra.png')
ruta_papel = os.path.join(BASE_DIR, 'static', 'img', 'papel.png')
ruta_tijera = os.path.join(BASE_DIR, 'static', 'img', 'tijera.png')

def creacion_juego(root:tk.Tk):

    # Definir tamaño deseado
    nuevo_ancho = 100
    nuevo_alto = 100

    # Abrir y redimensionar imágenes con PIL
    piedra_pil = Image.open(ruta_piedra).resize((nuevo_ancho, nuevo_alto))
    papel_pil = Image.open(ruta_papel).resize((nuevo_ancho, nuevo_alto))
    tijera_pil = Image.open(ruta_tijera).resize((nuevo_ancho, nuevo_alto))



    # Convertir a PhotoImage para Tkinter
    piedra_img = ImageTk.PhotoImage(piedra_pil)
    papel_img = ImageTk.PhotoImage(papel_pil)
    tijera_img = ImageTk.PhotoImage(tijera_pil)


    labelnombre = tk.Label(root,text="nombre")
    labelnombre.grid(row=1, column=0, sticky="e")

    input_nombre = tk.Entry(root)
    input_nombre.grid(row=1, column=1, padx=5, pady=5)


    # Agrega esto debajo de input_nombre
    tabla_resultados = ttk.Treeview(root, columns=("Jugador", "Usuario", "Consola", "Resultado"), show="headings", height=5)
    tabla_resultados.heading("Jugador", text="Jugador")
    tabla_resultados.heading("Usuario", text="Usuario")
    tabla_resultados.heading("Consola", text="Consola")
    tabla_resultados.heading("Resultado", text="Resultado")
    tabla_resultados.grid(row=6, column=0, columnspan=3, padx=5, pady=10)


    def cargar_tabla():
        for fila in tabla_resultados.get_children():
            tabla_resultados.delete(fila)
        partidas = obtener_partidas()
        for partida in partidas:
            tabla_resultados.insert("", "end", values=partida)
    def jugar(eleccion_jugador):
        nombre = input_nombre.get().strip()

        if not nombre:
            messagebox.showwarning("Falta nombre", "Por favor ingresa tu nombre.")
            return

        consola = random.choice(cachipun)

        if eleccion_jugador == consola:
            resultado = "empate"
        elif (eleccion_jugador == "piedra" and consola == "tijera") or \
             (eleccion_jugador == "papel" and consola == "piedra") or \
             (eleccion_jugador == "tijera" and consola == "papel"):
            resultado = "ganaste"
        else:
            resultado = "perdiste"

        messagebox.showinfo("Resultado", f"{nombre}, elegiste: {eleccion_jugador}\nConsola: {consola}\nResultado: {resultado}")

        guardar_partida(nombre, eleccion_jugador, consola, resultado)
        cargar_tabla()
        input_nombre.delete(0, tk.END)
    label_piedra = tk.Label(root, text="Piedra")
    label_piedra.grid(row=3, column=0, padx=5, pady=5)
    boton_piedra = tk.Button(root, image=piedra_img, command= lambda: jugar("piedra"))
    boton_piedra.grid(row=4, column=0, padx=5, pady=5)

    label_papel = tk.Label(root, text="papel")
    label_papel.grid(row=3, column=1, padx=5, pady=5)
    boton_papel = tk.Button(root, image=papel_img, command= lambda:jugar("papel"))
    boton_papel.grid(row=4, column=1, padx=5, pady=5)

    label_tijera = tk.Label(root, text="tijera")
    label_tijera.grid(row=3, column=2, padx=5, pady=5)
    boton_tijera = tk.Button(root, image=tijera_img, command= lambda: jugar("tijera"))
    boton_tijera.grid(row=4, column=2, padx=5, pady=5)
    # Necesario para que las imágenes se mantengan en memoria
    boton_piedra.image = piedra_img
    boton_papel.image = papel_img
    boton_tijera.image = tijera_img
    

    def limpiar_datos():
        respuesta = messagebox.askyesno("Confirmar limpieza", "¿Seguro que quieres borrar todos los datos?")
        if respuesta:
            limpiar_tabla_cachipun()
            messagebox.showinfo("Limpieza", "Todos los datos han sido borrados.")
            cargar_tabla()  # si tienes función para actualizar la tabla visible

    boton_limpiar = tk.Button(root, text="Limpiar datos", command=limpiar_datos, bg="red", fg="white")
    boton_limpiar.grid(row=10, column=1, pady=10)

