class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            pad = len(a) - len(b)
            b = ("0" * pad) + b
        elif len(b) > len(a):
            pad = len(b) - len(a)
            a = ("0" * pad) + a
        carry = "0"
        result = [None for _ in a]
        for i, (char_a, char_b) in enumerate(zip(reversed(a), reversed(b))):
            cur_char, carry = self.add_chars(char_a, char_b, carry)
            result[i] = cur_char
        if carry == "1":
            result.append(carry)
        return "".join(reversed(result))

    def add_chars(self, a: str, b: str, carry: str) -> (str, str):
        if a == b == carry == "0":
            return "0", "0"
        if a == b == carry == "1":
            return "1", "1"
        if a == "1":
            if b == carry == "0":
                return "1", "0"
            else:
                return "0", "1"
        if b == "1":  # already know that a == "0"
            if carry == "0":
                return "1", "0"
            else:  # implied a == "0", b == "1", carry == "1", so carry
                return "0", "1"
        if carry == "1":  # already know that a == b == "0":
            return "1", "0"
