class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_to_int = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        }
        s2 = s.replace("IV", "I"*4).replace("IX", "VIIII").replace("XL", "X"*4).replace("XC", "LXXXX").replace("CD", "C"*4).replace("CM", "DCCCC")
        numbers = [numeral_to_int[c] for c in s2]
        return sum(numbers)
