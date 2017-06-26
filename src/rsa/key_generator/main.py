from src.rsa.key_generator.keys import gen_keys
from src.rsa.key_generator.logger import log_results
from src.rsa.key_generator.primes import gen_prime


def main():
    p, q = gen_prime(), gen_prime()
    public_key, private_key, modulus = gen_keys(p, q)
    log_results(public_key, private_key, modulus)


if __name__ == '__main__':
    main()
