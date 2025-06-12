class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = float("-inf")
        for i in range(1, len(nums)):
            result = max(
                result,
                abs(nums[i]-nums[i-1])
            )
        result = max(result, abs(nums[-1]-nums[0]))
        return result
