import math


NUMBERS_TO_ROMAN = {
    1     : "I",
    5     : "V",
    10    : "X",
    50    : "L",
    100   : "C",
    500   : "D",
    1_000 : "M",
}


ROMAN_TO_NUMBERS = {
    v: k for (k, v) in NUMBERS_TO_ROMAN.items()
}


class Solution:
    def intToRoman(self, num: int) -> str:
        result = []
        while num > 0:
            numeral, subtract = one_round(num)
            result.append(numeral)
            num = subtract
        return "".join(result)


def one_round(x: int) -> (str, int):
    if x < 1:
        raise ValueError(f"Can't represent negative numbers as Roman numerals.")
    lead = most_significant_digit(x)
    if lead != 4 and lead != 9:
        for k, v in reversed(NUMBERS_TO_ROMAN.items()):
            if k <= x:
                return (v, x - k)
    else:
        for k, v in NUMBERS_TO_ROMAN.items():
            if k > x:
                if k == 5:
                    numeral = "IV"
                    return ("IV", x - 4)
                elif k == 10:
                    return ("IX", x - 9)
                elif k == 50:
                    return ("XL", x - 40)
                elif k == 100:
                    return ("XC", x - 90)
                elif k == 500:
                    return ("CD", x - 400)
                elif k == 1_000:
                    return ("CM", x - 900)
                else:
                    raise Exception("This should never happen, Eric messed up!")


def most_significant_digit(n):
    if n == 0:
        return 0
    # Take the absolute value to handle negative numbers
    n = abs(n)
    # Find the number of digits
    num_digits = int(math.log10(n))
    # Divide by 10^(num_digits) to isolate the MSD
    msd = n // (10 ** num_digits)
    return int(msd)
