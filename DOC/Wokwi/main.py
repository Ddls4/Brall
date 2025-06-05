"""
from machine import Pin
import time

time.sleep(0.1)  # Espera que el USB esté listo
print("Hola")

# Pines del teclado matricial
Horisontal_pin = [2, 3, 4, 5]
Vertical_pin = [6, 7, 8, 9]

# Definir las teclas del teclado
keys = [['1', '2', "3", "A"],  # 2
        ['4', '5', "6", "B"],  # 3
        ['7', '8', "9", "C"],  # 4
        ['*', '0', "#", "D"]]  # 5

print("Pines")

# Declarar los pines del teclado
cols = []
rows = []
for x in range(0, 4):
    rows.append(Pin(Horisontal_pin[x], Pin.OUT))
    rows[x].value(0)
    print("Pines declarados")
for x in range(0, 4):    
    cols.append(Pin(Vertical_pin[x], Pin.IN, Pin.PULL_DOWN))
    print("Pines declarados")

# Definir pines para el LED (o luces)
led_pins = [Pin(i, Pin.OUT) for i in [20, 21, 22, 19, 24, 25]]  # Luces en 6 pines diferentes

# Definición del alfabeto Braille básico
braille_dict = {
    'a': [1, 0, 0, 0, 0, 0],
    'b': [1, 1, 0, 0, 0, 0],
    'c': [1, 0, 0, 1, 0, 0],
    'd': [1, 0, 0, 1, 1, 0],
    'e': [1, 0, 0, 0, 1, 0],
    'f': [1, 1, 0, 1, 0, 0],
    'g': [1, 1, 0, 1, 1, 0],
    'h': [1, 1, 0, 0, 1, 0],
    'i': [0, 1, 0, 1, 0, 0],
    'j': [0, 1, 0, 1, 1, 0],
    'k': [1, 0, 1, 0, 0, 0],
    'l': [1, 1, 1, 0, 0, 0],
    'm': [1, 0, 1, 1, 0, 0],
    'n': [1, 0, 1, 1, 1, 0],
    'o': [1, 0, 1, 0, 1, 0],
    'p': [1, 1, 1, 1, 0, 0],
    'q': [1, 1, 1, 1, 1, 0],
    'r': [1, 1, 1, 0, 1, 0],
    's': [0, 1, 1, 1, 0, 0],
    't': [0, 1, 1, 1, 1, 0],
    'u': [1, 0, 1, 0, 0, 1],
    'v': [1, 1, 1, 0, 0, 1],
    'w': [0, 1, 0, 1, 1, 1],
    'x': [1, 0, 1, 1, 0, 1],
    'y': [1, 0, 1, 1, 1, 1],
    'z': [1, 0, 1, 0, 1, 1],
    ' ': [0, 0, 0, 0, 0, 0],
}

# Función para encender los LEDs según el patrón de Braille
def light_up_braille(braille):
    for i in range(6):
        led_pins[i].value(braille[i])

# Función para escanear el teclado
def scan_keypad():
    while True:
        for row_idx, row in enumerate(rows):
            row.high()
            for col_idx, col in enumerate(cols):
                if col.value() == 1:
                    time.sleep(0.1)  # Debounce
                    row.low()
                    return keys[row_idx][col_idx]
            row.low()

# Función para avanzar o retroceder en el array
def navigate_braille(braille_array, direction):
    if direction == "next":
        return braille_array[1:] + [braille_array[0]]
    elif direction == "prev":
        return [braille_array[-1]] + braille_array[:-1]

# Principal
word = "abcdefghij"  # Palabra inicial
braille_word = [braille_dict[char] for char in word]  # Convertir palabra a Braille
current_index = 0  # Indice del Braille actual

while True:
    print("Presiona una tecla...")

    # Escanear la tecla
    key = scan_keypad()
    print(f"Tecla presionada: {key}")
    
    # Si la tecla presionada es A, avanzar
    if key == 'A':
        current_index = (current_index + 1) % len(braille_word)
    
    # Si la tecla presionada es B, retroceder
    elif key == 'B':
        current_index = (current_index - 1) % len(braille_word)
    
    # Mostrar el Braille actual
    current_braille = braille_word[current_index]
    light_up_braille(current_braille)  # Activar LEDs según el Braille

    time.sleep(0.5)  # Esperar antes de escanear nuevamente
    """

from machine import Pin
import time

time.sleep(0.1)  # Espera que el USB esté listo
print("Hola")

# Pines del teclado matricial
Horisontal_pin = [2, 3, 4, 5]
Vertical_pin = [6, 7, 8, 9]

# Definir las teclas del teclado
keys = [['1', '2', "3", "A"],  # 2
        ['4', '5', "6", "B"],  # 3
        ['7', '8', "9", "C"],  # 4
        ['*', '0', "#", "D"]]  # 5

print("Pines")

# Declarar los pines del teclado
cols = []
rows = []
for x in range(0, 4):
    rows.append(Pin(Horisontal_pin[x], Pin.OUT))
    rows[x].value(0)
    print("Pines declarados")
for x in range(0, 4):    
    cols.append(Pin(Vertical_pin[x], Pin.IN, Pin.PULL_DOWN))
    print("Pines declarados")

# Definir un único LED
led = Pin(20, Pin.OUT)

# Función para escanear el teclado
def scan_keypad():
    while True:
        for row_idx, row in enumerate(rows):
            row.high()
            for col_idx, col in enumerate(cols):
                if col.value() == 1:
                    time.sleep(0.1)  # Debounce
                    row.low()
                    return keys[row_idx][col_idx]
            row.low()

# Función para encender o apagar el LED en relación con las teclas
def update_led(key):
    # Las teclas que corresponden a encender el LED
    toggle_keys = ['1', '2', '4', '5', '7', '8']
    
    # Si la tecla presionada está en las teclas de encendido, encender el LED
    if key in toggle_keys:
        led.value(1)
        time.sleep(3)
        led.value(0)
    else:
        led.value(0)

# Principal
while True:
    print("Presiona una tecla...")

    # Escanear la tecla
    key = scan_keypad()
    print(f"Tecla presionada: {key}")

    # Actualizar el estado del LED
    update_led(key)

    time.sleep(0.5)  # Esperar antes de escanear nuevamente
  