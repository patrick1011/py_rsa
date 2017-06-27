from tests.helpers.rsa_keys import PRIVATE_EXPONENT, MODULUS, CIPHERTEXT_FROM_UTF8

from server.services import decrypt


def fail_if_called(*args):
    assert False


def pass_if_called(*args):
    assert True


def test_decrypt_produces_a_string():
    plaintext = decrypt(ciphertext=CIPHERTEXT_FROM_UTF8,
                        private_exponent=PRIVATE_EXPONENT,
                        modulus=MODULUS,
                        not_unicode_handler=fail_if_called)
    assert type(plaintext) == str


def test_decrypt_fails_for_non_utf8_cipher():
    ciphertext_not_from_utf8 = 1000001
    plaintext = decrypt(ciphertext=ciphertext_not_from_utf8,
                        private_exponent=PRIVATE_EXPONENT,
                        modulus=MODULUS,
                        not_unicode_handler=pass_if_called)

    assert plaintext == None
