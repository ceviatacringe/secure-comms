# Symmetric Encryption Tool


https://github.com/ceviatacringe/secure-comms/assets/160585624/8175722d-8d13-4518-8121-364d95d21443

This is a Python-based symmetric encryption tool designed to secure your messages, especially when using proprietary software platforms. By encrypting your messages, you ensure that even if the platform accesses your data, and tries to breach your privacy by spying on your messages, it remains unreadable without the correct decryption key. This tool uses AES-256 encryption, providing a high level of security for your communications.

## Features

- **Secure Encryption**: Utilizes AES-256 for encryption.
- **Easy-to-Use**: Simple interface for encrypting and decrypting text.
- **Hotkey Support**: Encrypt and decrypt text using designated hotkeys.
- **Clipboard Integration**: Semi-automatically encrypts or decrypts clipboard contents.
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

In a long conversation, or multiple conversations, patters can be observed since short words and sentences are encrypted the same way each time while using the same keyword, so if somebody wanted to, they could analyze the patterns and try to figure out vague things based on behavioral analysis. They will not however be able to decrypt the data and read the messages themselves unless they have the keyword.
