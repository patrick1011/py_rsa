from src.key_generator.keys import gen_keys
from src.key_generator.log_keys import log_keys
from src.key_generator.primes import gen_prime


def main():
    """Generates keys for use with RSA encryption scheme.

    Run this file as a module from ./src using:

    python -m src.rsa.key_generator.main

    Method and algorithms are taken from 'Understanding Cryptography', A
    Textbook for Students and Practitioners by Christof Paar, Jan Pelzl,
    Bart Preneel (ISBN: 8601406549616).

    Primes are 512 bit.

    Side Effects:
        Prints public and private exponents and modulus to console.  To
        use with the Flask server paste the public exponent and modulus
        into src.conf.env
    """

    p, q = gen_prime(), gen_prime()
    public_exponent, private_exponent, modulus = gen_keys(p, q)
    log_keys(public_exponent, private_exponent, modulus)


if __name__ == '__main__':
    main()
