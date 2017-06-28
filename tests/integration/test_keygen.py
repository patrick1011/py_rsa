from key_generator.keys import EncryptionScheme
from key_generator.primes import gen_prime

from client.services import encrypt
from server.services import decrypt


def fail_if_called(*args):
    assert False


def test_keygen_makes_valid_keys():

    p = gen_prime(size=512)
    q = gen_prime(size=512)

    scheme = EncryptionScheme(prime_one=p,
                              prime_two=q)

    plaintext = 'hello world'

    ciphertext = encrypt(plaintext=plaintext,
                         public_exponent=scheme.public_exponent,
                         modulus=scheme.modulus)

    new_plaintext = decrypt(ciphertext=ciphertext,
                            private_exponent=scheme.private_exponent,
                            modulus=scheme.modulus,
                            not_unicode_handler=fail_if_called)

    # FIXME: have to do the below because decoding fills new_plaintext
    # with 'blank' unicode at the start of the string.  Doesn't effect
    # output when rendered on terminal but annoying.
    # Here new_plaintext = '\x00\x00\x00...00hello world'.

    cleaned_new_plaintext = new_plaintext[-len(plaintext):]

    assert cleaned_new_plaintext == plaintext
