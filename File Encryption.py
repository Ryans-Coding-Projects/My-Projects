#This program is used to encry/decrypt files

from cryptography.fernet import Fernet

def generate_and_save_key(key_file):
    with open(key_file, "wb") as file:
        file.write(Fernet.generate_key())

def load_key(key_file):
    with open(key_file, "rb") as file:
        return file.read()

def encrypt_decrypt_file(key, input_file, output_file, mode='encrypt'):
    cipher = Fernet(key)
    with open(input_file, "rb") as file:
        data = file.read()
        if mode == 'encrypt':
            processed_data = cipher.encrypt(data)
        else:
            processed_data = cipher.decrypt(data)
    with open(output_file, "wb") as file:
        file.write(processed_data)

