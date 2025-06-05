from time import sleep
import customtkinter
import speech_recognition as sr
import tkinter as tk
from tkinter import ttk

# Reconocedor de voz
r = sr.Recognizer()

# Función para enviar el texto
def Enviar():
    texto = Entry1.get()
    print("Enviado:", texto)
    # Aquí podrías enviar a la Raspberry Pi Pico por serial
    # ser = serial.Serial('COM3', 115200)
    # ser.write(texto.encode())
    # Entry1.delete(0, tk.END)

# Función para activar reconocimiento de voz y escribir en Entry1
def Voz():
    with sr.Microphone() as source:
        try:
            Entry1.delete(0, tk.END)
            Entry1.insert(0, "Escuchando...")
            root.update()
            audio_text = r.listen(source)
            t_aud = r.recognize_google(audio_text , language='es-ES')
            print("Reconocido:", t_aud)
            Entry1.delete(0, tk.END)
            Entry1.insert(0, t_aud)
        except:
            Entry1.delete(0, tk.END)
            Entry1.insert(0, "Lo siento, no entendí lo que dijiste")

# Crear la ventana principal
root = customtkinter.CTk()
root.geometry("450x300")  # Largo x Alto
root.title("Enviar datos a Raspberry Pi Pico")

# Frame de la interfaz
frm = ttk.Frame(root, padding=10)
frm.grid()

# Botones en la columna 0
customtkinter.CTkButton(frm, text="Voz", command=Voz, width=80, height=80).grid(column=0, row=0, pady=5)
customtkinter.CTkButton(frm, text="Enviar", command=Enviar, width=80, height=80).grid(column=0, row=1, pady=5)
customtkinter.CTkButton(frm, text="Quitar", command=root.destroy, width=80, height=80).grid(column=0, row=2, pady=5)

# Entry en la columna 1
Entry1 = customtkinter.CTkEntry(frm, width=300, height=250)
Entry1.grid(column=1, row=0, rowspan=3, padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()
