from math import gcd
from random import randint
import binascii



prime_one = prime_generator()
prime_two = prime_generator()

n = prime_one*prime_two

euleurs_phi = (prime_one - 1)*(prime_two - 1)
private_exponent = xgcd(euleurs_phi, public_exponent)
if (private_exponent < 0):
    private_exponent += euleurs_phi
