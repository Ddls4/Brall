import keyboard

print("Presioná cualquier tecla. ESC para salir.")

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        print(f"Tecla presionada: {event.name}")
        if event.name == 'esc':
            break