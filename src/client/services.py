import json
import os
import requests


def read_plaintext():
    """Reads plaintext_here.txt

    Additional inputs:
        src/client/plaintext_here.txt

    Returns:
        (str) contents of plaintext_here
    """
    with open('src/client/plaintext_here.txt') as plaintext:
        return plaintext.read()


def encrypt(message):
    """Encrypts message using RSA encryption scheme:

    ciphertext = plaintext**PUBLIC_EXPONENT % MODULUS

    Args:
        message (str || int): plaintext to be encrypted

    Environment variables:
        PUBLIC_EXPONENT (int): uri of the py_rsa server.
        MODULUS (int): public exponent of encryption scheme.

    Returns:
        Encrypted plaintext.
    """

    public_exponent = int(os.environ.get(key='PUBLIC_EXPONENT'))
    modulus = int(os.environ.get(key='MODULUS'))

    int_message = int.from_bytes(message.encode(), 'big')
    return pow(int_message, public_exponent, modulus)


def send(ciphertext):
    """Sends ciphertext to py_rsa server.

    Args:
        ciphertext (int): ciphertext to sent

    Environment variables:
        URI (str): uri of the py_rsa server.

    Side effects:
        Makes a post request to URI above.  Prints respose to terminal.
    """

    uri = os.environ.get(key='URI')

    payload = json.dumps({
        "ciphertext": ciphertext
    })
    r = requests.post(uri, data=payload)

    print(r.status_code)
