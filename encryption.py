from hashlib import sha256
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

# Define functions using adjusted imports
def generate_aes_key(keyword):
    return sha256(keyword.encode()).digest()

# Encrypt data
def encrypt(plaintext, keyword):
    key = generate_aes_key(keyword)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    iv = cipher.iv
    return (iv + ct_bytes).hex()

# Decrypt data
def decrypt(ciphertext_hex, keyword):
    key = generate_aes_key(keyword)
    iv_ct = bytes.fromhex(ciphertext_hex)
    iv = iv_ct[:16]
    ct = iv_ct[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
