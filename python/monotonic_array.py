from itertools import pairwise

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all(n1 <= n2 for n1, n2 in pairwise(nums)) or all(n1 >= n2 for n1, n2 in pairwise(nums))
