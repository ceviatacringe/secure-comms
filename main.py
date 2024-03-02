from menufunctions import *
from encryption import generate_aes_key
import colored
from hashlib import sha256
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

"""https://github.com/ceviatacringe/secure-comms/"""
# Same source code, just put it all in 1 script for compact compiling


DELAY = 0.007
green = colored.fg(10)
white = colored.fg(15)
red = colored.fg(1)

# Generate a 32-byte (256-bit) AES key from the keyword
def generate_aes_key(keyword: str) -> bytes:
    return sha256(keyword.encode()).digest()


# Encrypt data
def encrypt(plaintext: str, keyword: str) -> str:
    key = generate_aes_key(keyword)
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ct_bytes = cipher.encrypt(padded_plaintext)
    return ct_bytes.hex()


# Decrypt data
def decrypt(ciphertext_hex: str, keyword: str) -> str:
    key = generate_aes_key(keyword)
    ct_bytes = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ct_bytes)
    # Unpad the plaintext after decryption
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')

def main() -> None:
    encrypt_hotkey = 'insert'
    # Don't use a key that can be typed (use a function key)
    decrypt_hotkey = 'f2'
    keyword = input("Encryption key generation word: " + green)
    # Takes the decrypted text, and pastes it whever you're hovering so that you can see it directly in your app
    write_display = True
    clear()
    while True:
        # Print basic menu
        print(f"{white}Secure comms {colored.fg(8)}by ceviatacringe\n\n")
        print(f"{green}Keyword: {white}{keyword}")
        print(f"{green}Encrypt hotkey: {white}{encrypt_hotkey}")
        print(f"{green}Decrypt hotkey: {white}{decrypt_hotkey}\n")
        print(f"{green}1. {white}Start")
        print(f"{green}2. {white}Change keyword")
        print(f"{green}3. {white}Change encryption hotkey")
        print(f"{green}4. {white}Change decryption hotkey")
        if write_display:
            print(f"{green}5. {white}Write decrypted text: {green}{write_display}")
        else:
            print(f"{green}5. {white}Write decrypted text: {red}{write_display}")
        print(f"{green}6. {white}Instructions\n")
        print(f"{green}7. {white}Exit\n")
        # User input menu interaction
        choice = input()
        if choice == '1':
            # Runs main encryption/decryption loop
            clear()
            print(f"{green}Encrypt{white}: {encrypt_hotkey}")
            print(f"{green}Decrypt{white}: {decrypt_hotkey}\n\n")
            runner(encrypt_hotkey, decrypt_hotkey, keyword, DELAY, write_display)
        elif choice == '2':
            # Change keyword
            clear()
            keyword = input(f"{green}Update keyword: {white}")
            clear()
        elif choice == '3':
            # Change encrypt hotkey
            clear()
            encrypt_hotkey = get_hotkey()
            clear()
        elif choice == '4':
            # Change decrypt hotkey
            clear()
            decrypt_hotkey = get_hotkey()
            clear()
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
            print(f"{red}Exiting.{white}")
            break


if __name__ == "__main__":
    main()
