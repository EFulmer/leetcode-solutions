class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algo:
        # Basic idea: the solution is either the sum of everything seen
        # so far, or just the current number
        # (defining "everything seen so far" as the best sum so far.
        # So not necessarily A[0..i], but A[i..j])
        best_sum = float("-inf")
        current_sum = 0
        for num in nums:
            current_sum = max(current_sum + num, num)
            best_sum = max(current_sum, best_sum)
        return best_sum
