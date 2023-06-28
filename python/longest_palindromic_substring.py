class Solution:
    def palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        # some sort of n-wise sliding window thing?
        if self.palindrome(s):
            return s
        candidates = []
        for window_length in range(1, len(s)):
            for start in range(0, len(s)-window_length+1):
                substring = s[start:start+window_length]
                if self.palindrome(substring):
                    candidates.append(substring)
        if not candidates:
            return s[0]
        return candidates[-1]
