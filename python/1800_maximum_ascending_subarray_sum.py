class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        # What I would do here is:
        # 1. Get all the subarrays where values are ascending.
        # 2. Get all their sums.
        # 3. Return the maximum value computed in step 2.
        # (Steps 1 and 2 don't need to be done seperately, we can
        # get ascending SA's and then compute their sums as we
        # get each one)
        next_start, winner = get_ascending_subarray_sum_starting_from(nums, 0)
        while next_start < len(nums):
            next_start, contender = get_ascending_subarray_sum_starting_from(
                nums, next_start
            )
            winner = max(winner, contender)
        return winner


def get_ascending_subarray_sum_starting_from(
    xs: list[int], start: int
) -> tuple[int, int]:
    subarray_sum = last = xs[start]
    i = start + 1
    while i < len(xs):
        if xs[i] <= last:
            break
        else:
            last = xs[i]
            subarray_sum += last
        i += 1
    return i, subarray_sum
