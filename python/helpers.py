from math import log10
from typing import List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"


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


def knapsack(weights: list, values: list, capacity: int):
    if len(values) != len(weights):
        raise ValueError("should be one weight and value per item, no more, no less")
    solutions = [[0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
    for i in range(len(weights)):
        for w in range(capacity+1):
            if weights[i] <= w:
                solutions[i+1][w] = max(
                    solutions[i][w],
                    solutions[i][w - weights[i]] + values[i],
                )
            else:  # Exclude branch
                solutions[i+1][w] = solutions[i][w]
    return solutions


def shift_one_character_by(char: str, d: int) -> str:
    """Shift the ASCII lowercase char, `char` by `d` positions in the
    Latin alphabet.
    """
    # NOT `char`'s ASCII value,
    # but rather its index in `string.ascii_lowercase`.
    char_number = ord(char) - 97
    return string.ascii_lowercase[(char_number + d) % 26]
