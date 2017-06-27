from client.services import encrypt
from client.services import read_plaintext
from client.services import send

from client.settings import PUBLIC_EXPONENT, MODULUS, URI


def main():
    """Client for sending encrypted messages to a py_rsa server.

    Run this file as a module using:

    python -m client.main

    Variables required from settings.py:
        URI (str): uri of the py_rsa server.
        PUBLIC_EXPONENT (int): public exponent of encryption scheme.
        MODULUS (int): modulus of encryption scheme.

    Additional inputs:
        Messsage to be sent should be saved in plaintext_payload.txt.
    """

    plaintext = read_plaintext()

    ciphertext = encrypt(plaintext=plaintext,
                         public_exponent=PUBLIC_EXPONENT,
                         modulus=MODULUS)

    send(ciphertext=ciphertext,
         uri=URI)

if __name__ == '__main__':
    main()
