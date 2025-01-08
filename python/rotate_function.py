class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        sum_ = sum(nums)
        dp = [0] * N
        # F(0) is given as defined.
        dp[0] = sum(i * x for (i, x) in enumerate(nums))
        for i in range(1, N):
            # For all other F(i), we can figure out a recurrence
            # relation:
            # Going over the terms L-R:
            # dp[i-1]/F(i-1) contains "most" of the "information" we need
            # to compute F(i).
            # Every element of nums, aside the one at nums[N-i], has
            # its coefficient incremented by one. So we can add the sum
            # again.
            # Since N-i is being "rotated" to the back, that implies
            # that its former coefficient was N.
            # So we need to subtract (N - nums[N-i]) to get F(i).
            dp[i] = dp[i-1] + sum_ - N * nums[N-i]
        return max(dp)

# Since we only need F(i-1) at any point, we don't need the array.
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        sum_ = sum(nums)
        # F(0) is given as defined.
        previous = current_max = sum(i * x for (i, x) in enumerate(nums))
        for i in range(1, N):
            previous = contender = previous + sum_ - N * nums[N-i]
            if contender > current_max:
                current_max = contender
        return current_max
