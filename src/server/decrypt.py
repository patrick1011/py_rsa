import os


def decrypt(cypertext):
    private_exponent = int(os.environ.get(key='PRIVATE_EXPONENT'))
    modulus = int(os.environ.get(key='MODULUS'))

    plaintext = pow(cypertext, private_exponent, modulus)

    return plaintext.to_bytes((modulus.bit_length() + 7) // 8, 'big').decode()
