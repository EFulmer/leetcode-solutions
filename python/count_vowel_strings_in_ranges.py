from functools import cache


VOWELS = frozenset("aeiou")


@cache
def is_vowely(word: str) -> bool:
    return word[0] in VOWELS and word[-1] in VOWELS


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        is_word_vowely = [is_vowely(word) for word in words]
        # exploiting that True behaves as 1 in Python.
        prefix_sums = [0 for _ in range(len(words))]
        prefix_sums[0] = int(is_word_vowely[0])
        for i in range(1, len(words)):
            prefix_sums[i] = is_word_vowely[i] + prefix_sums[i-1]
        ans = []
        for (lb, rb) in queries:
            if lb == 0:
                ans.append(prefix_sums[rb])
            else:
                ans.append(prefix_sums[rb] - prefix_sums[lb-1])
        return ans
