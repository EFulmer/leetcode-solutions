def shift_one_character_by(char: str, d: int) -> str:
    """Shift the ASCII lowercase char, `char` by `d` positions in the
    Latin alphabet.
    """
    # NOT `char`'s ASCII value,
    # but rather its index in `string.ascii_lowercase`.
    char_number = ord(char) - 97
    return string.ascii_lowercase[(char_number + d) % 26]


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # Explanation:
        # The first N characters of s get shifted by
        # sum(shifts) - sum(shifts[:N])
        #
        # Or, in other words, every shift is applied to s[0],
        # every shift but the first is applied to s[1], ...
        #
        # So we can sum up the number of shifts to start, and decrease
        # it by shifts[i] after doing the "full shift" of s[i].
        acc = [None] * len(shifts)
        current_shift = sum(shifts)
        for i in range(len(acc)):
            acc[i] = shift_one_character_by(char=s[i], d=current_shift)
            current_shift -= shifts[i]
        return "".join(acc)
