class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        digits = []
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            negative = False
            s = s[1:]
        else:
            negative = False

        for c in s:
            if not c.isdigit():
                break
            else:
                digits.append(c)
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
