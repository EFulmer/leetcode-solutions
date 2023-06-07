from string import ascii_lowercase, ascii_uppercase


class Solution:
    # using string module
    def detectCapitalUse(self, word: str) -> bool:
        return all(c in ascii_lowercase for c in word) or \
            all(c in ascii_uppercase for c in word) or \
            (word[0] in ascii_uppercase and all(c in ascii_lowercase for c in word[1:]))
    # using methods of str type
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
