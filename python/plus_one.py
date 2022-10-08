class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # First, copy the list since the problem spec doesn't say it can be mutated
        # (and this is also generally a good practice)
        result = digits[:]
        n = len(result) - 1
        carry = 1
        while n > -1 and carry > 0:
            result[n] += carry
            if result[n] == 10:
                result[n] = 0
                carry = 1
            else:
                carry = 0
            n -= 1
        # If there's still a carry after getting to the most significant digit,
        # add a 1 to the start of the number
        if carry > 0:
            result.insert(0, 1)
        return result
