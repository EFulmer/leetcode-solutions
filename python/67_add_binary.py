class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Strategy:
        # convert the strings to decimal integers, add them,
        # then convert the result to binary and return it.
        a_int = int(a, 2)
        b_int = int(b, 2)
        return bin(a_int+b_int)[2:]
