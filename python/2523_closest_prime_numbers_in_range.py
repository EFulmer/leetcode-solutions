import itertools
from typing import List


UPPER_BOUND = 10**6 + 1


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        s = sieve(UPPER_BOUND)
        primes = itertools.takewhile(
            lambda x: x <= right,
            itertools.dropwhile(lambda x: x < left, s)
        )
        prime_diffs = (
            ([x, y], y - x)
            for x, y in n_wise(primes)
        )
        try:
            return min(prime_diffs, key=lambda x: x[1])[0]
        except ValueError:
            return [-1, -1]

def sieve(upper_bound: int):
    if upper_bound < 2:
        return []

    is_prime = [True] * upper_bound
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(upper_bound**0.5) + 1):
        if is_prime[i]:
            for j in range(i**2, upper_bound, i):
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]


def n_wise(gen, n=2):
    return zip(
        *(itertools.islice(g, i, None)
        for i, g in enumerate(itertools.tee(gen, n)))
    )
