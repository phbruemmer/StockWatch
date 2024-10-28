import base64
import os


def generate_private_key():
    return os.urandom(32)


def encrypt(data, private_key):
    data_bytes = data.encode()
    padded_data = data_bytes.ljust(32, b'\0')[:32]
    encrypted_bytes = bytes(a ^ b for a, b in zip(padded_data, private_key))
    encrypted_base64 = base64.urlsafe_b64encode(encrypted_bytes).decode()
    return encrypted_base64


def decrypt(data, private_key):
    encrypted_bytes = base64.urlsafe_b64decode(data)
    decrypted_bytes = bytes(a ^ b for a, b in zip(encrypted_bytes, private_key))
    decrypted_string = decrypted_bytes.decode().rstrip('\0')
    return decrypted_string