class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Strategy:
        # convert the strings to decimal integers, add them,
        # then convert the result to binary and return it.
        a_int = int(a, 2)
        b_int = int(b, 2)
        return bin(a_int+b_int)[2:]


# Actual arithmetic solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_length, b_length = len(a), len(b)
        if a_length > b_length:
            b = ('0' * (a_length - b_length)) + b
        elif a_length < b_length:
            a = ('0' * (b_length - a_length)) + a
        result = []
        carry = None
        for c1, c2 in zip(reversed(a), reversed(b)):
            # Add carry, c1, and c2
            if c1 == '1' and c2 == '1':
                if carry:
                    carry = '1'
                    result.append('1')
                else:
                    carry = '1'
                    result.append('0')
            elif c1 == '0' and c2 == '0':
                if carry:
                    carry = None
                    result.append('1')
                else:
                    result.append('0')
            else:  # a zero and a one
                if carry:
                    carry = '1'
                    result.append('0')
                else:
                    result.append('1')
        if carry == '1':
            result.append(carry)
        return "".join(reversed(result))
