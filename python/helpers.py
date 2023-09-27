from math import log10
from typing import List


def num_digits_in_int(n: int) -> int:
    return trunc(log10(n)) + 1

def list_of_ints_to_int(l: List[int]) -> int:
    m = len(l)
    return sum(
        n * 10**(m-i-1)
        for i, n in enumerate(l)
    )

def list_of_digits(x):
    l = num_digits_in_int(x)
    result = []
    while l > 0:
        current_digit = x // 10**(l-1)
        result.append(current_digit)
        x = x - (current_digit * 10**(l-1))
        l -= 1
    return result
