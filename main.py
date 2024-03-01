import os
from menufunctions import *
from encryption import generate_aes_key

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    encrypt_hotkey = 'insert'
    decrypt_hotkey = 'home'
    keyword = input("Encryption key generation word: ")
    clear()
    while True:
        print(f"Keyword: {keyword}")
        print(f"Encrypt hotkey: {encrypt_hotkey}")
        print(f"Decrypt hotkey: {decrypt_hotkey}\n")
        print("1. Change keyword")
        print("2. Change encryption hotkey")
        print("3. Change decryption hotkey")
        print("4. Instructions")
        print("5. Exit\n")

        choice = input()

        if choice == '1':
            clear()
            keyword = input("Update keyword: ")
        elif choice == '2':
            clear()
            encrypt_hotkey = get_hotkey()
        elif choice == '3':
            clear()
            decrypt_hotkey = get_hotkey()
        elif choice == '4':
            clear()
            instructions()
        elif choice == '5':
            clear()
            print("Exiting.")
            break

if __name__ == "__main__":
    main()
