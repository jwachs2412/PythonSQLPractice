def is_prime(start, stop):
    primes = []
    for num in range(start, stop + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    print(", ".join(str(p) for p in primes))


is_prime(10000, 10050)
