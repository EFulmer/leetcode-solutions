# o(nums, current_step) = { if current_step == len(nums) then 0
#                         { else it's however far back the last step you can reach gets you
#                         {


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1
        inf = 1_000_000
        dp = [inf for _ in nums]
        dp[-1] = 0
        for i in range(len(dp)-2, -1, -1):
            if nums[i] != 0:
                # If the end of `nums` is within `i` steps maximum,
                # we already know that dp[i] should be 1. 
                if nums[i] + i >= len(nums):
                    dp[i] = 1
                else:
                    dp[i] = 1 + min(dp[i+1:i+nums[i]+1])
        return dp[0]
