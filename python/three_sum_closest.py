class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # First, sort the array.
        nums = sorted(nums)  # not in-place to avoid messing with test harness

        # Since it's guaranteed that there's no match, we can't just track
        # the current best, but also the difference between the CB
        # and the target
        # Reason being: tracking the CB is one point of information.
        # When there's 3 (as in 3 sum), you can't reconstruct the rest
        # from just the CB. You need at least two.
        current_best = sum(nums[:3])
        current_best_delta = abs(target - current_best)

        for i, n in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                contender = n + nums[j] + nums[k]
                contender_delta = abs(contender - target)
                if contender_delta < current_best_delta:
                    current_best_delta = contender_delta
                    current_best = contender

                if contender >= target:
                    k = k - 1
                else:
                    j = j + 1

        return current_best
