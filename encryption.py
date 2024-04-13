from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
import base64

def generate_aes_key(password: str, salt: bytes, key_size: int = 32) -> bytes:
    return PBKDF2(password, salt, dkLen=key_size, count=100000)

def encrypt(plaintext: str, password: str) -> str:
    salt = base64.b64encode(get_random_bytes(16)).decode('utf-8')
    key = generate_aes_key(password, base64.b64decode(salt))
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ct_bytes = cipher.encrypt(padded_plaintext)
    # Add the salt into the final plaintext
    return salt + base64.b64encode(iv + ct_bytes).decode('utf-8')

def decrypt(ciphertext_b64: str, password: str) -> str:
    # Get the salt out of the original message 
    salt = base64.b64decode(ciphertext_b64[:24])
    iv_and_ct = base64.b64decode(ciphertext_b64[24:])
    iv = iv_and_ct[:16]
    ct_bytes = iv_and_ct[16:]
    key = generate_aes_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ct_bytes)
    plaintext = unpad(padded_plaintext, AES.block_size)
    return plaintext.decode('utf-8')
