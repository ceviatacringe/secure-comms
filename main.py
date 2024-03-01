import os
from hotkey import get_hotkey
from encryption import generate_key

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    hotkey = ''
    while True:
        print(f"Current hotkey: {hotkey}")
        print("1. Change keyword")
        print("2. Change hotkey")
        print("3. Instructions")
        print("4. Exit\n")

        choice = input()

        if choice == '1':
            clear()
        elif choice == '2':
            clear()
            hotkey = get_hotkey()
        elif choice == '3':
            clear()
        elif choice == '4':
            clear()
            print("Exiting.")
            break

if __name__ == "__main__":
    main()
