import json
from cryptography.fernet import Fernet

def load_key(path="key.key"):
    with open(path, "rb") as key_file:
        return key_file.read()

def encrypt_data(filepath, data, key):
    f = Fernet(key)
    json_data = json.dumps(data).encode()
    encrypted = f.encrypt(json_data)
    with open(filepath, "wb") as file:
        file.write(encrypted)

def decrypt_data(filepath, key):
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted = file.read()
    decrypted = f.decrypt(encrypted)
    return json.loads(decrypted.decode())
