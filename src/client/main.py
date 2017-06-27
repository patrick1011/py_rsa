from src.client.services.encrypt import encrypt
from src.client.services.read_plaintext import read_plaintext
from src.client.services.send import send


def main():
    """Client for sending encrypted messages to a py_rsa server.

    Run this file as a module from ./src using:

    python -m src.client.main

    Environment variables required:
        URI (str): uri of the py_rsa server.
        PUBLIC_EXPONENT (int): public exponent of encryption scheme.
        MODULUS (int): modulus of encryption scheme.

    Additional inputs:
        Messsage to be sent should be saved in plaintext.txt.

    Side effects:
        Prints response from rsa py_rsa server to terminal.
    """

    plaintext = read_plaintext()
    ciphertext = encrypt(plaintext)
    send(ciphertext)

if __name__ == '__main__':
    main()
