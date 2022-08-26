from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        magazine = Counter(magazine)
        return magazine >= note
