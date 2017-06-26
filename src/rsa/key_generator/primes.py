from random import randint

from src.rsa.constants import (RSA_PRIME_SIZE, SECURITY_PARAMETER)


def generate_rsa_primes(*args):
    return (
        prime_generator(),
        prime_generator()
    )


def prime_generator():
    candidate = randint(1, 2**RSA_PRIME_SIZE)
    is_prime = fermat_primality_test(candidate, SECURITY_PARAMETER)
    return candidate if is_prime else prime_generator()


def fermat_primality_test(candidate, security_parameter):
    if candidate == 2:
        return True
    if candidate % 2 == 0:
        return False
    for i in range(security_parameter):
        a = randint(1, candidate-1)
        if pow(a, candidate-1, candidate) != 1:
            return False
    return True
