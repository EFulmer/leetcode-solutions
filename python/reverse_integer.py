import math


MIN_INT = -2 ** 31
MAX_INT = 2 ** 31 - 1


def get_number_of_digits(x: int) -> int:
    """Get the number of digits in base 10 integer `x`."""
    return math.floor(math.log10(x)) + 1


def get_nth_digit(x: int, n: int) -> int:
    """Get the `n`-th digit, starting from the most significant, of base
    10 integer `x`.

    get_nth_digit(123, 1) == 3
    get_nth_digit(123, 2) == 2
    get_nth_digit(123, 3) == 1
    """
    # To get the nth digit, first get rid of all digits before the
    # `n`-th by doing floor division with `10**(n-1)`, which removes all
    # digits less significant than `n`:
    digits_from_nth = x // 10**(n-1)
    # then get rid of everything after the `n`-th digit by modulo-ing
    # the remaining digits with 10, which eliminates all digits aside
    # the least significant of what remains
    return digits_from_nth % 10


def get_sign(x: int) -> int:
    """Get the sign coeffecient of integer `x`."""
    return -1 if x < 0 else 1


class Solution:
    def reverse(self, x: int) -> int:
        # 0 is handled as a special case since `log(0)` is undefined:
        if x == 0:
            return 0
        # Compute the absolute value and sign of `x` since logarithms
        # of negative numbers are also undefined, but
        # `reverse(-x) == -1 * reverse(x)`:
        sign = get_sign(x)
        x = abs(x)

        result = 0
        # Compute the number of digits in `x` just once, since we
        # reference it multiple times:
        m = get_number_of_digits(x)
        for n in range(0, m):
            # The `n`-th digit of `reverse(x)` is the `m-n`-th digit of
            # `x`:
            # (this loop could be a one-liner with `sum`, but that
            # implementation turned out slightly slower in my tests)
            result += get_nth_digit(x, n+1) * 10**(m-n-1)
        # Set the sign of the result:
        result *= sign
        # And zero it out if it's out of the acceptable range:
        # (this could probably be made more efficient at the expense of
        # readability, since you don't need to compute the entirety of
        # `reverse(x)` to know if it's out of the range)
        if not MIN_INT < result < MAX_INT:
            return 0
        return result
