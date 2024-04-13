# Symmetric Encryption Tool


https://github.com/ceviatacringe/secure-comms/assets/160585624/8175722d-8d13-4518-8121-364d95d21443

This is a Python-based symmetric encryption tool designed to secure your messages, especially when using proprietary software platforms. By encrypting your messages, you ensure that even if the platform accesses your data, and tries to breach your privacy by spying on your messages, it remains unreadable without the correct decryption key. This tool uses AES-256 encryption, providing a high level of security for your communications.

## Features

- **Secure Encryption**: Utilizes AES-256 for encryption.
- **Salting** Each identical message has a different encrypted output
- **Easy-to-Use**: Simple interface.
- **Hotkey Support**: Use hotkeys for conveniency and efficiency
- Cool colors 🥳

## Installation

### Option 1:
Download the latest release and use the .exe

### Option 2:
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository or download the source code.
3. Install required dependencies:

    ```bash
    pip install pycryptodome colored pyperclip keyboard
    ```

## Instructions

1. Open your main communication app (discord, whatsapp, whatever you use)
2. Write some text in the text field, then press your encryption hotkey to encrypt and send it (insert by default)
3. Hover over the text and press the decryption hotkey to decrypt the text (F2 by default.)
to encrypt or decrypt text copied to the clipboard.

- If `write display` is enabled, you the decrypted text will be pasted in the text field for ease of view
- Use function keys for your hotkeys, otherwise it will interfere with the process and fail (F2, F3, INSERT, END, etc...)
- If you're using this to talk to someone, make sure you have the same keyword, otherwise it won't work.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Security disclaimer

The security of this app hinges on the strength of the initial passkey, which can be brute forced, all though I implemented measures against brute forcing, it's still possible.
