import math


MIN_INT = -2 ** 31
MAX_INT = 2 ** 31 - 1


def get_number_of_digits(x: int) -> int:
    return math.floor(math.log10(x)) + 1


def get_nth_digit(x: int, n: int) -> int:
    """Get the n-th digit, starting from the most significant, of a base 10 number.
    get_nth_digit(123, 1) == 3
    get_nth_digit(123, 2) == 2
    get_nth_digit(123, 3) == 1
    """
    # to get the nth digit, we get rid of everything before the nth digit by doing a floor division with 10^(n-1)
    digits_from_nth = x // 10**(n-1)
    # then get rid of everything after the n-th digit by modulo-ing it with 10
    return digits_from_nth % 10


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0
        m = get_number_of_digits(x)
        for n in range(0, m):
            result += get_nth_digit(x, n+1) * 10**(m-n-1)
        result *= sign
        if result < MIN_INT or result > MAX_INT:
            return 0
        return result
