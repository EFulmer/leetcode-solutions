from typing import List


# Solution with builtins: just use sorted and provide a key that's just
# whether the numbers are odd. Make the key a function rather than a
# lambda for a slight performance boost.
def odd(x):
    return x % 2


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=odd)

# "Intended" solution: use two pointers, one to where the
# "odds section" starts, and one to where the "evens section" ends.
# Starting from the beginning of the array check each item.
# If it's even, great, no work to be done, up your marker/pointer for
# where the "evens section" ends.
# If it's odd, move it to the start of the "odds section" and bring
# that pointer down one.
# In-place for memory efficiency.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # traverse the array, keeping track of where the evens begin
        # when you find an odd, swap it with the last item and check again
        even_section_end = 0
        odd_section_start = len(nums) - 1
        while even_section_end < odd_section_start:
            if nums[even_section_end] % 2 != 0:
                nums[even_section_end], nums[odd_section_start] = nums[odd_section_start], nums[even_section_end]
                odd_section_start -= 1
            else:
                even_section_end += 1
        return nums


# List comprehension, not-in-place version:
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens = [num for num in nums if num % 2 == 0]
        odds = [num for num in nums if num % 2 == 1]
        return evens + odds

# More efficient non-in-place version:
# adopting the two pointers approach ("even section end" and
# "odd section start"), but using them for a new array
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = [None for _ in nums]
        # traverse the array, keeping track of where the evens begin
        # when you find an odd, swap it with the last item and check again
        even_section_end = 0
        odd_section_start = len(nums) - 1
        for i, n in enumerate(nums):
            if n % 2 == 0:
                result[even_section_end] = n
                even_section_end += 1
            elif n % 2 == 1:
                result[odd_section_start] = n
                odd_section_start -= 1
        return result
