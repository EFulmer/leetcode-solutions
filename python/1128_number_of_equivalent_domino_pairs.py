from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = collections.Counter()
        result = 0
        for i in range(1, len(dominoes)):
            prev = tuple(sorted(dominoes[i-1]))
            cur = tuple(sorted(dominoes[i]))
            seen[prev] += 1
            result += seen[cur]
        return result
