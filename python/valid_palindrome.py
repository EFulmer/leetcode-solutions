# stdlib and string-slicing solution:
from string import ascii_letters

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join(char.lower() for char in s if char in ascii_letters or char in digits)
        return s2 == s2[::-1]


# two pointer solution:
from string import ascii_lowercase, digits

class Solution:
    def isPalindrome(self, s: str) -> bool:
        acceptable = set(ascii_lowercase) | set(digits)
        start_index = 0
        end_index = len(s) - 1
        while start_index < end_index:
            if s[start_index].lower() not in acceptable:
                start_index += 1
                continue
            elif s[end_index].lower() not in acceptable:
                end_index -= 1
                continue
            elif s[start_index].lower() != s[end_index].lower():
                return False
            else:
                start_index += 1
                end_index -= 1
        return True
