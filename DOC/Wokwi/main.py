from machine import Pin
import time

time.sleep(0.1)
print("Sistema Braille iniciado")

# Pines del teclado matricial
Horisontal_pin = [2, 3, 4, 5]
Vertical_pin = [6, 7, 8, 9]

# Definir las teclas del teclado
keys = [['1', '2', "3", "A"],
        ['4', '5', "6", "B"],
        ['7', '8', "9", "C"],
        ['*', '0', "#", "D"]]

# Inicializar filas y columnas
rows = [Pin(pin, Pin.OUT) for pin in Horisontal_pin]
cols = [Pin(pin, Pin.IN, Pin.PULL_DOWN) for pin in Vertical_pin]

# LED para mostrar Braille (por ejemplo, en pin 20)
led = Pin(20, Pin.OUT)

# Diccionario Braille con 6 puntos por letra
braille_dict = {
    'a': [1, 0, 0, 0, 0, 0],
    'b': [1, 0, 1, 0, 0, 0],
    'c': [1, 1, 0, 0, 0, 0],
    'd': [1, 1, 0, 1, 0, 0],
    'e': [1, 0, 0, 1, 0, 0],
    'f': [1, 1, 1, 0, 0, 0],
    'g': [1, 1, 1, 1, 0, 0],
    'h': [1, 0, 1, 1, 0, 0],
    'i': [0, 1, 1, 0, 0, 0],
    'j': [0, 1, 1, 1, 0, 0],
    'k': [1, 0, 0, 0, 1, 0],
    'l': [1, 0, 1, 0, 1, 0],
    'm': [1, 1, 0, 0, 1, 0],
    'n': [1, 1, 0, 1, 1, 0],
    'o': [1, 0, 0, 1, 1, 0],
    'p': [1, 1, 1, 0, 1, 0],
    'q': [1, 1, 1, 1, 1, 0],
    'r': [1, 0, 1, 1, 1, 0],
    's': [0, 1, 1, 0, 1, 0],
    't': [0, 1, 1, 1, 1, 0],
    'u': [1, 0, 0, 0, 1, 1],
    'v': [1, 0, 1, 0, 1, 1],
    'w': [0, 1, 1, 1, 0, 1],
    'x': [1, 1, 0, 0, 1, 1],
    'y': [1, 1, 0, 1, 1, 1],
    'z': [1, 0, 0, 1, 1, 1],
    ' ': [0, 0, 0, 0, 0, 0],
}

# Texto inicial a mostrar en Braille
texto = "hola"
print("Texto a mostrar en Braille:", texto)

# Convertir texto a lista de patrones Braille
braille_letras = [braille_dict[letra] for letra in texto]
indice_actual = 0

# Función para escanear teclado
def scan_keypad():
    for row_idx, row in enumerate(rows):
        row.high()
        for col_idx, col in enumerate(cols):
            if col.value() == 1:
                time.sleep(0.2)
                row.low()
                return keys[row_idx][col_idx]
        row.low()
    return None

# Mostrar letra en Braille con LED
def mostrar_braille(patron):
    print("Braille:", patron)
    for punto in patron:
        if punto == 1:
            led.value(1)  # Encender el LED
            time.sleep(0.3)  # Mantener encendido por 0.3 segundos
            led.value(0)  # Apagar el LED
        else:
            time.sleep(0.3)  # Pausa sin encender el LED
        time.sleep(0.2)  # Pausa entre puntos Braille
    time.sleep(0.5)  # Pausa entre letras

# Función para validar si una tecla es correcta
def validar_tecla(tecla, patron_braille):
    # Teclas válidas corresponden a las posiciones 1, 2, 4, 5, 7, 8
    posiciones_validas = {
        '1': 0,  # 1 corresponde al primer punto
        '2': 1,  # 2 corresponde al segundo punto
        '4': 2,  # 4 corresponde al tercer punto
        '5': 3,  # 5 corresponde al cuarto punto
        '7': 4,  # 7 corresponde al quinto punto
        '8': 5   # 8 corresponde al sexto punto
    }

    # Si la tecla es válida, verificamos si el patrón Braille tiene un 1 en la posición correspondiente
    if tecla in posiciones_validas:
        posicion = posiciones_validas[tecla]
        if patron_braille[posicion] == 1:
            return True
    return False

# Bucle principal
while True:
    print("Presiona A o B para avanzar a la siguiente letra...")

    tecla = None
    while not tecla:
        tecla = scan_keypad()

    print(f"Tecla presionada: {tecla}")

    if tecla in ['A', 'B']:  # Avanzar con A o B
        letra_braille = braille_letras[indice_actual]
        mostrar_braille(letra_braille)

        # Avanzar a la siguiente letra
        indice_actual = (indice_actual + 1) % len(braille_letras)

    elif validar_tecla(tecla, braille_letras[indice_actual]):  # Validar las teclas 1,2,4,5,7,8
        print(f"Tecla {tecla} correcta: LED encendido!")
        led.value(1)
        time.sleep(0.3)  # Mantener el LED encendido por 0.3 segundos
        led.value(0)
    else:
        print(f"Tecla {tecla} incorrecta!")
