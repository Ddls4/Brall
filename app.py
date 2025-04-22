import keyboard
import sounddevice as sd
import numpy as np
import time

# Palabra y sus letras
palabra = "hola"
letras = list(palabra)
indice = 0

# Glosario de teclas Braille
teclas_braille = {
    '7': 1,
    '8': 4,
    '4': 2,
    '5': 5,
    '1': 3,
    '2': 6,
}
braille_por_letra = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6]
}

# Función para generar un beep
def beep(frequency=440, duration=0.2, samplerate=44100):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate)
    sd.wait()

print("Usá D para avanzar, A para retroceder por la palabra.")
print("Presioná teclas numéricas (numpad) para reproducir puntos Braille de la letra actual.")
print("ESC para salir.")

while True:
    event = keyboard.read_event()

    # Avanzar
    if event.event_type == keyboard.KEY_DOWN and event.name.lower() == 'd':
        if indice < len(letras) - 1:
            indice += 1
        print(f"Letra actual: {letras[indice]}")
        time.sleep(0.2)

    # Retroceder
    elif event.event_type == keyboard.KEY_DOWN and event.name.lower() == 'a':
        if indice > 0:
            indice -= 1
        print(f"Letra actual: {letras[indice]}")
        time.sleep(0.2)

    # Tecla Braille presionada
    elif event.event_type == keyboard.KEY_DOWN and event.name in teclas_braille:
        letra_actual = letras[indice].lower()
        punto_presionado = teclas_braille[event.name]
        puntos_validos = braille_por_letra.get(letra_actual, [])

        if punto_presionado in puntos_validos:
            print(f"Punto Braille válido ({punto_presionado}) para letra '{letra_actual}'")
            beep(frequency=300 + punto_presionado * 100, duration=0.15)
        else:
            print(f"Punto Braille {punto_presionado} NO pertenece a la letra '{letra_actual}'")

    elif event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
        print("Saliendo...")
        break