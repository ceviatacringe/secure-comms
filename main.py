from menufunctions import *
from encryption import generate_aes_key

# Delay time (seconds) between virtual keyboard usage 
# The lower the faster, too low and it might break depending on your specs.
DELAY = 0.005


def main():
    encrypt_hotkey = 'insert'
    decrypt_hotkey = 'f2'
    keyword = input("Encryption key generation word: ")
    # Takes the decrypted text, and pastes it whever you're hovering so that you can see it directly in your app
    write_display = True
    clear()
    while True:
        # Print basic menu
        print(f"Keyword: {keyword}")
        print(f"Encrypt hotkey: {encrypt_hotkey}")
        print(f"Decrypt hotkey: {decrypt_hotkey}\n")
        print("1. Start")
        print("2. Change keyword")
        print("3. Change encryption hotkey")
        print("4. Change decryption hotkey")
        print(f"5. Write decrypted text: {write_display}")
        print("6. Instructions\n")
        print("7. Exit\n")
        # User input menu interaction
        choice = input()
        if choice == '1':
            # Runs main encryption/decryption loop
            clear()
            print(f"Encrypt: {encrypt_hotkey}")
            print(f"Decrypt: {decrypt_hotkey}")
            runner(encrypt_hotkey, decrypt_hotkey, keyword, DELAY, write_display)
        elif choice == '2':
            # Change keyword
            clear()
            keyword = input("Update keyword: ")
            clear()
        elif choice == '3':
            # Change encrypt hotkey
            clear()
            encrypt_hotkey = get_hotkey()
        elif choice == '4':
            # Change decrypt hotkey
            clear()
            decrypt_hotkey = get_hotkey()
        elif choice == '5':
            # Updates the option for write_display
            write_display = not write_display
            clear()
        elif choice == '6':
            # Print instructions
            clear()
            instructions(encrypt_hotkey, decrypt_hotkey)
            clear()
        elif choice == '7':
            # Exit
            clear()
            print("Exiting.")
            break


if __name__ == "__main__":
    main()
