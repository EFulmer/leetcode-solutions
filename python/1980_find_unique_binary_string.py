class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Reasoning:
        #
        # 1. Each number being unique in binary means that it's also
        #    unique in decimal, since they are different waysto
        #    represent the same number.
        # 2. Storing them in a set allows for fast membership check.
        #    Storing them as a set of integers _should_ (not certain)
        #    be faster than as strings.
        # 3. We know what the largest allowed number is by the number
        #    of digits.
        # 4. With these pieces of info, we can just iterate through all
        #    numbers from 0 to 2**digits (2 as the base since binary)
        #    and return the first one that isn't in the provided list.
        # 5. From there, it's just about formatting.
        #
        # This solution will work just as well in any other language,
        # though in languages without built-in set types like C you'd
        # either keep the array (O(n) membership check for each) or
        # write your own. Not sure about how the trade-off of
        # converting an array/list/vector to a set once vs. a linear
        # time membership check each time looks.
        digits = len(nums[0])
        numbers = {to_decimal(n) for n in nums}
        for i in range(2**digits):
            if i not in numbers:
                return format_decimal(i, digits)


to_decimal = lambda x: int(x, 2)


def format_decimal(n, digits):
    # [2:] chops off the '0b'
    binary = bin(n)[2:]
    return binary.zfill(digits)
