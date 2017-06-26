from math import gcd

from src.rsa.constants import MINIMUM_PUBLIC_EXPONENT

from src.rsa.key_generator.extended_euclidian import extended_euclidian


def generate_keys_from_primes(primes):
    prime_one, prime_two = primes
    phi = (prime_one - 1)*(prime_two - 1)
    modulus = prime_one*prime_two

    public_exponent = generate_public_exponent(phi)
    private_exponent = generate_private_exponent(phi, public_exponent)

    return {
        'public': {
            'modulus': modulus,
            'exponent': public_exponent
        },
        'private': {
            'modulus': modulus,
            'exponent': private_exponent
        }
    }


def generate_public_exponent(phi, candidate=MINIMUM_PUBLIC_EXPONENT):
    is_relative_prime = (gcd(candidate, phi) == 1)
    if is_relative_prime:
        return candidate
    else:
        return generate_public_exponent(phi, candidate+1)


def generate_private_exponent(phi, public_exponent):
    exponent = extended_euclidian(phi, public_exponent)
    is_positive = (exponent > 0)
    return exponent if is_positive else exponent + phi
