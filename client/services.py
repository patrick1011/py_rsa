import json
import requests


def read_plaintext():
    """Reads plaintext_payload.txt

    Additional inputs:
        src/client/plaintext_payload.txt

    Returns:
        (str) contents of plaintext_payload
    """

    with open('client/plaintext_payload.txt') as plaintext:
        # return plaintext.read()
        return 'hello world'


def encrypt(plaintext, public_exponent, modulus):
    """Encrypts message using RSA encryption scheme:

    ciphertext = plaintext**PUBLIC_EXPONENT % MODULUS

    Args:
        message (str || int): plaintext to be encrypted
        public_exponent (int): public exponent of encryption scheme.
        modulus (int): modulus of encryption scheme.

    Returns:
        Encrypted plaintext.
    """

    int_plaintext = int.from_bytes(plaintext.encode(), 'big')

    ciphertext = pow(int_plaintext, public_exponent, modulus)

    return ciphertext


def send(ciphertext, uri):

    """Sends ciphertext to py_rsa server.

    Args:
        ciphertext (int): ciphertext to sent.
        uri (str): uri of the py_rsa server.

    Side effects:
        Makes a post request to URI above.  Prints respose to terminal.
    """

    payload = json.dumps({
        "ciphertext": ciphertext
    })

    r = requests.post(uri, data=payload)

    print(r.status_code, r.text)
