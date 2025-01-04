import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Our algorithm:
        # Figure out the first and last appearance indexes of each char.
        # For every character that appears more than once:
        # acc += the number of unique characters that appear between its
        # first and last appearance, (can also be char itself)
        # there are certain optimizations which we can come up with here like using bits and bit vectors
        # but this solution is clear IMO
        first_appearance = {
            c: None
            for c in string.ascii_lowercase
        }
        last_appearance = first_appearance.copy()
        # get both appearances
        for i, char in enumerate(s):
            if first_appearance[char] is None:
                first_appearance[char] = i
            last_appearance[char] = i

        result = 0

        for char in string.ascii_lowercase:
            first_index = first_appearance.get(char)
            if first_index is None:
                continue
            last_index = last_appearance.get(char)
            unique_chars_in_between = {
                char2 for char2 in s[first_index+1:last_index]
            }
            result += len(unique_chars_in_between)

        return result
