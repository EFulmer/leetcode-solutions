def score_split(s, i):
    return sum(1 for c in s[:i] if c == "0") \
        + sum(1 for c in s[i:] if c == "1")


class Solution:
    def maxScore(self, s: str) -> int:
        return max(score_split(s, i) for i in range(1, len(s)))
