class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Sliding window:
        # Count the number of consecutive unique numbers, after
        # sorting the array.
        # With those, you need to count the number of joins you need
        # to do, which is the number of consecutive uniques minus the
        # length of each run of uniques.
        # Then the result is n - that number (since worst case is you
        # need to change every number).
        n = len(nums)
        result = n
        xs = list(sorted(set(nums)))
        consecutive_uniques = 0

        for i, x in enumerate(xs):
            while consecutive_uniques < len(xs) and xs[consecutive_uniques] < x + n:
                consecutive_uniques += 1

            run_length = consecutive_uniques - i
            result = min(result, n-run_length)

        return result
