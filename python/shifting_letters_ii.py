def shift_one_character_by(char: str, d: int) -> str:
    """Shift the ASCII lowercase char, `char` by `d` positions in the
    Latin alphabet.
    """
    # NOT `char`'s ASCII value,
    # but rather its index in `string.ascii_lowercase`.
    char_number = ord(char) - 97
    return string.ascii_lowercase[(char_number + d) % 26]


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # The trick here, to avoid a quadratic-time solution, is to
        # build an array which stores the difference in indices shifted
        # from diff[i], diff[i+1], and track how that changes during
        # the actual process of shifting the chars.
        # i.e., start assuming that the distance is 0
        # and diff[0], diff[1] = 1, 0.
        # in this case, you would shift the first two chars of s
        # one forward each.
        # If diff[2] = -1, then you wouldn't shift the second char
        # at all.
        diff_from_last = [0] * len(s)
        for (start, end, direction) in shifts:
            if direction == 0:
                diff_from_last[start] -= 1
                if (end + 1) < len(s):
                    diff_from_last[end+1] += 1
            else:
                diff_from_last[start] = diff_from_last[start] + 1
                if (end + 1) < len(s):
                    diff_from_last[end+1] -= 1
        result = list(s)
        distance = 0
        for i in range(len(s)):
            distance = (distance + diff_from_last[i])
            result[i] = shift_one_character_by(s[i], distance)
        return "".join(result)
