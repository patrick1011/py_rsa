def extended_euclidian(a, b):
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
