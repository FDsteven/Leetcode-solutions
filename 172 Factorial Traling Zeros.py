def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    output = 0
    factorial = 1
    if n > 0:
        for i in range(1,n+1):
            factorial *= i
    while factorial % 10 == 0:
        factorial /= 10
        output += 1
    return output



n = 3
n = 5
n = 3
print(trailingZeroes(n))