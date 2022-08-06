class Solution:
    def myAtoi(self, s: str) -> int:
        # base case: if the string is empty or pure whitespace, return 0
        s = s.lstrip()
        if not s:
            return 0

        # otherwise, check for a sign:
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            negative = False
            s = s[1:]
        else:
            negative = False

        # collect the digits
        digits = []
        for c in s:
            if not c.isdigit():
                break
            else:
                digits.append(c)

        # and sum up the result:
        result = 0
        for position, digit in zip(range(0, len(digits)), reversed(digits)):
            result = result + (10**position) * int(digit)
        if negative:
            result = -result
        if result < -2**31:
            result = -2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1
        return result
