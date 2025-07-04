from cryptography.fernet import Fernet
import os

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    encrypted_path = file_path + '.enc'
    with open(encrypted_path, 'wb') as f:
        f.write(encrypted)
    return encrypted_path
