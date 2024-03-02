import keyboard
import os
import time
from encryption import *
import pyperclip


def clear():
    # Clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')


def get_hotkey():
    # Update hotkey
    print("Press a key to use it as your hotkey")
    time.sleep(0.2)
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # Check if the key is pressed down
        key = event.name
        return key


def instructions(encrypt_hotkey: str, decrypt_hotkey: str) -> None:
    # Print instructions
    print("The keyword generates an encryption key.")
    print("To decrypt a message, you need to use the same key that was used to encrypt it.")
    print("If you and somebody else have the same key, you can send messages back and forth.\n")
    print("\n\nEncryption:\nWrite text in a communication app (such as discord)")
    print(f"Press your encryption hotkey ({encrypt_hotkey}) to encrypt and send a message")
    print("\n\nDecryption:\nHover over the encrypted text (drag with your cursor)")
    print(f"Press your decryption hotkey ({decrypt_hotkey}) for it to decrypt")
    print('If you have "write decrypted text" enabled:')
    print("It will paste it in your discord text bar so that you can read it without checking the terminal")
    input("\n\nPress enter to exit...")


def copy(delay: float) -> None:
    # Copy selection to keyboard
    keyboard.press_and_release('control+a')
    time.sleep(delay)
    keyboard.press_and_release('control+c')


def runner(encrypt_hotkey: str, decrypt_hotkey: str, keyword: str, delay: float, DISPLAY: bool) -> None:
    while True:
        # Scan for hotkey
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == encrypt_hotkey:
                # Save the current clipboard
                normal_clipboard = pyperclip.paste()
                print("Encrypting")
                # Copy text from selection
                copy(delay)
                time.sleep(0.02)
                # Encrypt selection
                encrypted = encrypt(pyperclip.paste(), keyword)
                # Type Encrypted text
                keyboard.press_and_release('control+a')
                keyboard.write(encrypted)
                # Send encrypted text
                keyboard.press_and_release('enter')
                # Reset to the old clipboard
                pyperclip.copy(normal_clipboard)
            elif event.name == decrypt_hotkey:
                # Save the current clipboard
                normal_clipboard = pyperclip.paste()
                print("Decrypting")
                # Get selection
                keyboard.press_and_release('control+c')
                time.sleep(0.12)
                # Decrypt
                try:
                    decrypted = decrypt(pyperclip.paste(),keyword)
                    print(decrypted)
                    if DISPLAY:
                        keyboard.write(decrypted)
                except:
                    print("Invalid key or selection ")
                # Reset to the old clipboard
                pyperclip.copy(normal_clipboard)
            elif event.name == 'esc':
                break
                

        