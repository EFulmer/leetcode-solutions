class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, x in enumerate(nums):
            complement = target - x
            if complement in d:
                return d[complement], i
            else:
                d[x] = i
