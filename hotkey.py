import keyboard

def get_hotkey():
    print("Press a key to use it as your hotkey")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # Check if the key is pressed down
        key = event.name
        return key
