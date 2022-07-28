# Obvious stdlib solution:
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# implementing your own counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # short circuit
        if len(s) != len(t):
            return False
        s_counter, t_counter = dict(), dict()
        for c in s:
            s_counter[c] = s_counter.get(c, 0) + 1
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1
        return t_counter == s_counter
