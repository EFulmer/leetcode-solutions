class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Dynamic programming solution:
        # Let N := len(nums)
        # and also let DP[i] = True if there is a "path" from i to the end, False otherwise
        # But, how do we determine DP[i]?
        # Start with DP[N-1] = True (true by default, we're already at the end)
        # then DP[N-2] is True if nums[N-2] >= 1 (1 because we need to hop at least one index up)
        # How about the general case?
        # DP[i] := any(DP[j] for j in range(1, nums[i]))
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            current = nums[i]
            candidates = dp[i:i+current+1]
            if any(candidates):
                dp[i] = True
        return dp[0]
