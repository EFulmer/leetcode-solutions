class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(pref)
        words = sorted(words, key=len)
        words = (word for word in words if len(word) >= N)
        result = 0
        for word in words:
            result += word.startswith(pref)
        return result
