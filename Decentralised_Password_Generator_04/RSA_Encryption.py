# Encrypting and decrypting
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding



# Reading the keys back in (for demonstration purposes)
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

def encryption(message):

    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    #message = b'encrypt me!'
    # f = open('test.txt', 'rb')
    # message = f.read()
    # f.close()
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print(encrypted)
    return encrypted



encryption(b"Hello World")

# the name of the output instance is encrypted
