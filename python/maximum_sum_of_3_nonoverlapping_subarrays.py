class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        cand_window_one_start   = window_one_start   = 0
        cand_window_two_start   = window_two_start   = k
        cand_window_three_start = window_three_start = k * 2
        sum_one = sum_two = sum_three = -1
        pair_starts   = [window_one_start, window_two_start]
        triple_starts = [*pair_starts, window_three_start]

        N = len(nums)
        last_index = N - k
        while cand_window_three_start <= last_index:
            cand_sum_one   = sum(nums[cand_window_one_start:cand_window_one_start+k])
            cand_sum_two   = sum(nums[cand_window_two_start:cand_window_two_start+k])
            cand_sum_three = sum(nums[cand_window_three_start:cand_window_three_start+k])

            if cand_sum_one > sum_one:
                sum_one          = cand_sum_one
                window_one_start = cand_window_one_start
            if cand_sum_two + sum_one > sum_two:
                sum_two          = cand_sum_two + sum_one
                window_two_start = cand_window_two_start
                pair_starts      = [window_one_start, window_two_start]
            if cand_sum_three + sum_two > sum_three:
                sum_three          = cand_sum_three + sum_two
                window_three_start = cand_window_three_start
                triple_starts      = [*pair_starts, window_three_start]

            cand_window_one_start   += 1
            cand_window_two_start   += 1
            cand_window_three_start += 1

        return triple_starts
