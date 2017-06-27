from tests.helpers.rsa_keys import PUBLIC_EXPONENT, MODULUS

from client.services import encrypt


def test_encrypt_produces_an_int():
    ciphertext = encrypt(plaintext='hello world',
                         public_exponent=PUBLIC_EXPONENT,
                         modulus=MODULUS)
    assert type(ciphertext) == int
