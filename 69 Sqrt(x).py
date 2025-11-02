def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    i = 1
    if x < 2:
        return x
    while i <= x:
        if i ** 2 > x:
            return i - 1
        i += 1
    return 0

x = 4
print(mySqrt(x))