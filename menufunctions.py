import keyboard
import os
import time
from encryption import *
import pyperclip


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_hotkey():
    print("Press a key to use it as your hotkey")
    time.sleep(0.2)
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # Check if the key is pressed down
        key = event.name
        return key


def instructions():
    print("The keyword generates an AES key.")
    print("The key is used to encrypt messages over plaintext")
    print("If you and somebody else have the same key, you can send messages back and forth.\n")
    input("Press enter to exit...")


def copy(delay):
    keyboard.press_and_release('control+a')
    time.sleep(delay)
    keyboard.press_and_release('control+c')


def runner(encrypt_hotkey, decrypt_hotkey, keyword, delay):
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == encrypt_hotkey:
                print("Encrypting")
                copy(delay)
                time.sleep(0.02)
                encrypted = encrypt(pyperclip.paste(), keyword)
                keyboard.press_and_release('control+a')
                keyboard.write(encrypted)
                keyboard.press_and_release('enter')
            elif event.name == decrypt_hotkey:
                print("Decrypting")
                keyboard.press_and_release('control+c')
                time.sleep(0.05)
                try:
                    print(decrypt(pyperclip.paste(),keyword))
                except:
                    print("Invalid key or selection ")

        