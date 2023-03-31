import concurrent.futures as cf
import math

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with cf.ProcessPoolExecutor() as executor:
        # executor.map returns an iterator (one element per original element)
        # so we zip it with the original to sorta index it. Q: Will map()
        # always be 1:1?
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("%d is prime: %s" % (number, prime))


if __name__ == "__main__":
    main()
