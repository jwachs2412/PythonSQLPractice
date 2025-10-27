import math


def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False

    # Check for divisibility from 3 up to the square root of n,
    # incrementing by 2 to only check odd numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    # If no divisors are found, the number is prime
    return True


print(is_prime(20))
