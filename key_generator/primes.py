from random import randint


def gen_prime(size, sec=1000):
    """Generates prime by creating random number and checking primality
    with fermat test.

    Args:
        size (int): bit-size of prime (defualt 512)
        sec (int): security parameter for fermat primality test

    Primes are approx 512 bits by default.

    Returns:
        (int) Prime
    """

    while True:
        c = randint(1, 2**size)
        is_prime = fermat_prime_test(c, sec)
        if is_prime:
            return c


def fermat_prime_test(c, sec):
    """Fermat's prime test for PROBABALISTIC test of primality

    Args:
        c (int): candidate prime
        sec (int): security parameter

    Uses Fermat's little theorem which says if c is prime a^(c-1) = 1 mod c
    for a not divisible by c. Algorithm tests above equality sec times for
    random a's.

    Returns:
        bool indicating primality of c
    """

    if c == 2:
        return True
    if c % 2 == 0:
        return False
    for i in range(sec):
        a = randint(1, c-1)
        if pow(a, c-1, c) != 1:
            return False
    return True
