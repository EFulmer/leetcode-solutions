class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
        # Explained in plain English:
        # Consider [1, 2, 3]; next permutation is [1, 3, 2].
        # 1. Starting from the end of the array, find the first item k
        #    that's strictly less than the one after it
        #    (in this case, 2, or index 1)
        # 2. If the entire array is in ascending order, reverse it.
        #    (sort in desc.)
        # 3. Otherwise, also starting from the end of the array, find
        #    the first item j that's strictly greater than the item at
        #    k. In our example k would be index 1 and j would be index
        #    2.
        # 4. Swap the items at indices k and j, so we now have
        #    [1, 3, 2].
        # 5. Reverse the rest of the array starting from k+1.
        n = len(nums)
        k = n-2
        while k > -1:
            if nums[k] < nums[k+1]:
                break
            k = k - 1
        if k == -1:
            nums.sort()
            return

        l = n - 1
        while l > k:
            if nums[k] < nums[l]:
                break
            l = l - 1

        nums[k], nums[l] = nums[l], nums[k]
        nums[k+1:] = nums[:k:-1]
