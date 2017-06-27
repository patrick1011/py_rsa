from key_generator.keys import EncryptionScheme
from key_generator.log_keys import log_keys
from key_generator.primes import gen_prime


def main():
    """Generates keys for use with RSA encryption scheme and logs to termianl.

    Run this file as a module using:

    python -m key_generator.main

    Method and algorithms are taken from 'Understanding Cryptography', A
    Textbook for Students and Practitioners by Christof Paar, Jan Pelzl,
    Bart Preneel (ISBN: 8601406549616).

    Uses 512 bit primes.

    Side Effects:
        Prints public and private exponents and modulus to console.  To
        use with the Flask server paste the public exponent and modulus
        into server/settings/py
    """

    p = gen_prime(size=512)
    q = gen_prime(size=512)

    new_scheme = EncryptionScheme(prime_one=p,
                                  prime_two=q)

    log_keys(public_exponent=new_scheme.public_exponent,
             private_exponent=new_scheme.private_exponent,
             modulus=new_scheme.modulus)


if __name__ == '__main__':
    main()
