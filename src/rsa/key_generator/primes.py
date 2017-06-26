from random import randint

from src.rsa.constants import (RSA_PRIME_SIZE, SECURITY_PARAMETER)


def gen_prime(size=RSA_PRIME_SIZE, sec=SECURITY_PARAMETER):
    while True:
        c = randint(1, 2**size)
        is_prime = fermat_prime_test(c, sec)
        if is_prime:
            return c


def fermat_prime_test(c, sec):
    if c == 2:
        return True
    if c % 2 == 0:
        return False
    for i in range(sec):
        a = randint(1, c-1)
        if pow(a, c-1, c) != 1:
            return False
    return True
