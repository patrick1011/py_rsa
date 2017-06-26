from math import gcd

from src.rsa.key_generator.extended_euclidian import extended_euclidian


def gen_keys(p, q):
    """Generates keys for RSA encryption

    Args:
        p (int): prime
        q (int): prime

    Returns:
        Public and private exponents and modulus.
    """

    phi = (p - 1)*(q - 1)
    modulus = p*q

    public_exponent = gen_public(phi)
    private_exponent = gen_private(phi, public_exponent)

    return public_exponent, private_exponent, modulus


def gen_public(phi):
    """Generates public RSA exponent

    Args:
        phi (int): Euler's totient

    Returns:
        Public exponent
    """

    c = 3
    while True:
        is_relative_prime = (gcd(c, phi) == 1)
        if is_relative_prime:
            return c
        c += 2


def gen_private(phi, public):
    """Generates private RSA exponent using extended_euclidian

    Args:
        phi (int): Euler's totient
        public (int): Public exponent

    Returns:
        Public exponent
    """

    private = extended_euclidian(phi, public)
    return private if (private > 0) else private + phi
