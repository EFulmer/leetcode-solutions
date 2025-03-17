class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # We need to find the offset/pivot k. We can use that to
        # split the array into two and do a binary search on the
        # half of the array that will contain the target if it is in
        # the array.
        # Short-circuit for the case of nums being a one-element array:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        # Find the pivot:
        low = 0
        high = n - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low

        # Search in the appropriate half
        if nums[pivot] <= target <= nums[n-1]:
            return binary_search(nums, pivot, n-1, target)
        else:
            return binary_search(nums, 0, pivot-1, target)


def binary_search(ns: list[int], low: int, high: int, target: int) -> int:
    while low <= high:
        mid = (low + high) // 2
        if ns[mid] == target:
            return mid
        elif ns[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
