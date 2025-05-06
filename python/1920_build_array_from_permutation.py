class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [None] * (n := len(nums))
        for i in range(n):
            result[i] = nums[nums[i]]
        return result
