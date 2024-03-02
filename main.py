from menufunctions import *
from encryption import generate_aes_key

# Delay time (seconds) between virtual keyboard usage 
# The lower the faster, too low and it might break depending on your specs.
DELAY = 0.005


def main():
    encrypt_hotkey = 'insert'
    decrypt_hotkey = 'f2'
    keyword = input("Encryption key generation word: ")
    clear()
    while True:
        print(f"Keyword: {keyword}")
        print(f"Encrypt hotkey: {encrypt_hotkey}")
        print(f"Decrypt hotkey: {decrypt_hotkey}\n")
        print("1. Start")
        print("2. Change keyword")
        print("3. Change encryption hotkey")
        print("4. Change decryption hotkey")
        print("5. Instructions\n")
        print("6. Exit\n")

        choice = input()

        if choice == '1':
            clear()
            print(f"Encrypt: {encrypt_hotkey}")
            print(f"Decrypt: {decrypt_hotkey}")
            runner(encrypt_hotkey, decrypt_hotkey, keyword, DELAY)
        elif choice == '2':
            clear()
            keyword = input("Update keyword: ")
        elif choice == '3':
            clear()
            encrypt_hotkey = get_hotkey()
        elif choice == '4':
            clear()
            decrypt_hotkey = get_hotkey()
        elif choice == '5':
            clear()
            instructions()
        elif choice == '6':
            clear()
            print("Exiting.")
            break

if __name__ == "__main__":
    main()
