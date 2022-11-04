from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from RSA_Encryption import  padding, hashes, encryption

def Decrypt():

    with open("private_key.pem", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # This will return thr encrypted message in the encrypted variable
    encrypted = encryption(b"Hello World")
    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(original_message)
    print(str(original_message.decode('utf-8')))

    return original_message


Decrypt()

# The name of the decrypted instance is decrypted