class EncryptionScheme:
    def __init__(self, prime_one, prime_two):
        """Generates keys for RSA encryption.

        Args:
            prime_one (int): prime number
            prime_two (int): prime number

        Instantiated class has attributes:
            modulus (int) Scheme modulus.
            public_exponent (int) Public exponent used to encrypt.
            private_exponent (int) Private exponent used to decrypt.
        """

        phi = (prime_one - 1)*(prime_two - 1)

        self.modulus = prime_one * prime_two
        self.public_exponent = self.gen_public(phi)
        self.private_exponent = self.gen_private(phi, self.public_exponent)

    def gen_public(self, phi):
        """Generates public RSA exponent

        Args:
            phi (int): Euler's totient

        Returns:
            Public exponent
        """

        c = 3
        while True:
            is_relative_prime = (self.gcd(c, phi) == 1)
            if is_relative_prime:
                return c
            c += 2

    def gen_private(self, phi, public_exponent):
        """Generates private RSA exponent using extended_euclidian

        Args:
            phi (int): Euler's totient
            public (int): Public exponent

        Returns:
            Public exponent
        """

        private_exponent = self.extended_euclidian(phi, public_exponent)

        if (private_exponent > 0):
            return private_exponent
        return private_exponent + phi

    def gcd(self, a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """

        while b:
            a, b = b, a % b
        return a

    def extended_euclidian(self, a, b):
        """Extended euclidian algorithm

        Given a and b computes x and y such that:

        a*x + b*y = gcd(a,b)

        Args:
            a (int)
            b (int)

        Returns:
            y from above
        """

        x, next_x, y, next_y = 1, 0, 0, 1
        while b != 0:
            q = a // b
            next_x, x = x - q * next_x, next_x
            next_y, y = y - q * next_y, next_y
            a, b = b, a % b
        return y
