import math


def factors(n):
    return [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]


def isPrime(n):

    # Corner case
    if (n <= 1):
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True

print(max(list(filter(isPrime, factors(600851475143)))))