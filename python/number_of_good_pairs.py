from itertools import combinations


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(1 for (i, j) in combinations(nums, r=2) if i == j)
