from key_generator.primes import fermat_prime_test as prime_test
from key_generator.primes import gen_prime


def test_prime_generates_small_primes():
    candidate = gen_prime(size=10)
    very_probably_prime = prime_test(candidate, sec=1000)

    assert very_probably_prime


def test_prime_generates_large_primes():
    candidate = gen_prime(size=512)
    very_probably_prime = prime_test(candidate, sec=1000)

    assert very_probably_prime
