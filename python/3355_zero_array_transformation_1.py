class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Running each "query" against the array is O(n^2)
        # If we merge the queries into a difference/step array, we
        # have two O(n) operations, or just O(n) runtime and O(n) space
        # we can make a "step array", where whenever the values change,
        # you apply that value to all indices up until the value
        # changes again
        step_array = [0] * (n := len(nums))
        for l, r in queries:
            # starting at l, subtract 1 from each number
            step_array[l] -= 1
            # if the right-hand boundary isn't the end of the
            # array, we "step back up" there since we only
            # -1 for items in [l, r] inclusive.
            if r + 1 < n:
                step_array[r+1] += 1
        i = 0
        cur_diff = 0
        while i < n:
            if step_array[i] != 0:
                cur_diff += step_array[i]
            nums[i] += cur_diff
            # We don't need to go through the whole array.
            # Since we only look at each array element once,
            # if it's > 0 after applying the aggregated transformation
            # we know we've "lost"
            if nums[i] > 0:
                return False
            i += 1
        return True
