from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        expected = sum(range(n))
        actual = sum(nums)
        return expected - actual
