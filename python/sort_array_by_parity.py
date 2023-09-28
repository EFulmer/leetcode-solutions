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
