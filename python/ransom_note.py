from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)
        magazine = Counter(magazine)
        return magazine >= note


# second solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        tally = [0 for _ in range(26)]
        for char in magazine:
            tally[ord(char) - 97] += 1

        for char in ransomNote:
            i = ord(char) - 97
            if tally[i] <= 0:
                return False
            tally[i] -= 1
        return True<Paste>
