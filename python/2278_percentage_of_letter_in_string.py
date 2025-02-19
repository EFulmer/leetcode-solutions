import math


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = sum(1 for char in s if char == letter)
        return math.floor(count / len(s) * 100)
