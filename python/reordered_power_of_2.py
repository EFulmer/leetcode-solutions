import itertools
import math


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n_string = str(n)
        n_string_sorted = "".join(sorted(n_string))
        valid_permutations = (p for p in itertools.permutations(n_string_sorted) if p[0] != "0")
        for permutation in valid_permutations:
            permutation_ = int("".join(permutation))
            if math.log2(permutation_).is_integer():
                return True
        return False
