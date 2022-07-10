from itertools import islice, tee


nwise = lambda g, n=2: zip(*(islice(g, i, None) for i, g in enumerate(tee(g, n))))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        len_s = len(s)
        if len_s == len(set(s)):
            return len_s
        for i in range(1, len_s):
            unique_substrings = (
                x for x in nwise(s, i)
                if len(set(x)) == len(x)
            )
            try:
                next(unique_substrings)
                result = i
            except StopIteration:
                break
        return result
