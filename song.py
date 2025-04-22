import keyboard  # Librería para detectar las teclas
import sounddevice as sd
import numpy as np
import wave

# Función para cargar el archivo WAV
def play_wav(file_path):
    with wave.open(file_path, 'rb') as wf:
        # Lee el archivo WAV
        data = wf.readframes(wf.getnframes())
        # Convierte los datos a un array numpy
        audio_data = np.frombuffer(data, dtype=np.int16)
        # Reproduce el sonido
        sd.play(audio_data, wf.getframerate())
        sd.wait()

def beep(frequency=440, duration=0.2, samplerate=44100):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, samplerate)
    sd.wait()
    
sound_file = "so.wav"  # Cambia a tu archivo .wav

while True:
    if keyboard.is_pressed("a"):  # Si se presiona la tecla "A"
        beep(frequency=300 + 1 * 100, duration=0.15)  # Reproduce el sonido