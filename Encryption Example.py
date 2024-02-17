import os
from cryptography.hazmat.primitives.ciphers import Cipher , algorithms , modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def encrypt_file( input_file , output_file , key ) :
    with open(input_file , 'rb') as file :
        plaintext = file.read()
        print(plaintext)
    # Pad the plaintext to meet block size requirements
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Create an AES cipher object
    cipher = Cipher(algorithms.AES(key) , modes.ECB() , backend = default_backend())

    # Encrypt the padded data
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted content to a new file
    with open(output_file , 'wb') as file :
        file.write(ciphertext)


def encrypt_folder( input_folder , output_folder , key ) :
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder) :
        os.makedirs(output_folder)

    # Encrypt each file in the input folder and save to the output folder
    for root , _ , files in os.walk(input_folder) :
        for file_name in files :
            input_file_path = os.path.join(root , file_name)
            output_file_path = os.path.join(output_folder , file_name + '.encrypted')

            encrypt_file(input_file_path , output_file_path , key)


# Example usage
key = b'Sixteen byte key'
input_folder = 'toEncrypte'
output_folder = 'encrypted_output_folder'

# Encrypt the content of the folder and save to a new folder
encrypt_folder(input_folder , output_folder , key)
print(f"Encryption complete. Encrypted content saved to '{output_folder}'.")
