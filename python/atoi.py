INTMIN = -2**31
INTMAX = 2**31 - 1


class Solution:

    def myAtoi(self, s: str) -> int:
        # base case: if the string is empty or pure whitespace, return 0
        s = s.lstrip()
        if not s:
            return 0

        # otherwise, check for a sign:
        if s[0] == "-":
            sign = -1
            start_index = 1
        elif s[0] == "+":
            sign = 1
            start_index = 1
        else:
            sign = 1
            start_index = 0

        # collect the digits
        digits = []
        cur_index = start_index
        while cur_index < len(s):
            c = s[cur_index]
            if not c.isdigit():
                break
            else:
                digits.append(c)
                cur_index = cur_index + 1

        # and sum 'em up:
        result = 0
        for position, digit in zip(range(len(digits)-1, -1, -1), digits):
            result = result + (10**position) * int(digit)

        result = result * sign
        result = min(max(result, INTMIN), INTMAX)
        return result
