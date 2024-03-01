import keyboard

def get_hotkey():
    print("Press a key to use it as your hotkey")
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # Check if the key is pressed down
        key = event.name
        return key

def instructions():
    print("The keyword generates an AES key.")
    print("The key is used to encrypt messages over plaintext")
    print("If you and somebody else have the same key, you can send messages back and forth.\n")
    input("Press enter to exit...")