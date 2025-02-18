import functools
import itertools


NUMBERS = "123456789"


class Solution:
    def smallestNumber(self, pattern: str) -> str:
        pred = functools.partial(predicate, pattern=pattern)
        all_possible_permutations = itertools.permutations(
            NUMBERS, len(pattern)+1
        )
        candidates = sorted(
            [perm for perm in all_possible_permutations if pred(perm)]
        )
        return "".join(candidates[0])


def predicate(item: tuple[str], pattern: str) -> bool:
    for (i, c) in enumerate(pattern):
        if c == "I":
            if item[i] >= item[i+1]:
                return False
        elif c == "D":
            if item[i] <= item[i+1]:
                return False
        else:
            raise ValueError(
                f"expected every character in pattern to be either " \
                "'I' or 'D', got {c}"
            )
    return True
