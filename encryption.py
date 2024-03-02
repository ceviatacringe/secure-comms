from hashlib import sha256
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad


# Generate a 32-byte (256-bit) AES key from the keyword
def generate_aes_key(keyword):
    return sha256(keyword.encode()).digest()


# Encrypt data
def encrypt(plaintext, keyword):
    key = generate_aes_key(keyword)
    cipher = AES.new(key, AES.MODE_ECB)
    # Pad the plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ct_bytes = cipher.encrypt(padded_plaintext)
    return ct_bytes.hex()


# Decrypt data
def decrypt(ciphertext_hex, keyword):
    key = generate_aes_key(keyword)
    ct_bytes = bytes.fromhex(ciphertext_hex)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ct_bytes)
    # Unpad the plaintext after decryption
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')

