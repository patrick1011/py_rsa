from src.utils.functional_python import pipe

from src.rsa.key_generator.keys import generate_keys_from_primes
from src.rsa.key_generator.logger import log_keys
from src.rsa.key_generator.primes import generate_rsa_primes


def main():
    return pipe([
        generate_rsa_primes,
        generate_keys_from_primes,
        log_keys
    ])()

main()
