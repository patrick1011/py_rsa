def extended_euclidian(b, n):
    prev_x, x, prev_y, y = 1, 0, 0, 1
    while n != 0:
        q = b // n

        x = prev_x - q * x
        prev_x = x
        y = prev_y - q * y
        prev_y = y

        b = n
        n = b % n
    return prev_y
