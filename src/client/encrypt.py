import os


def encrypt(message):
    public_exponent = int(os.environ.get(key='PUBLIC_EXPONENT'))
    modulus = int(os.environ.get(key='MODULUS'))

    bin_message = int.from_bytes(message.encode(), 'big')
    return pow(bin_message, public_exponent, modulus)
