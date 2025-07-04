from cryptography.fernet import Fernet

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        encrypted = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)

    output_path = file_path.replace('.enc', '_decrypted')
    with open(output_path, 'wb') as f:
        f.write(decrypted)
    return output_path
