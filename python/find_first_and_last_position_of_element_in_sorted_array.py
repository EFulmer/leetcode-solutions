def binary_search(xs: List[int], low: int, high: int, needle: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if xs[mid] == needle:
            return mid
        elif xs[mid] > needle:
            return binary_search(xs=xs, low=low, high=mid-1, needle=needle)
        elif xs[mid] < needle:
            return binary_search(xs=xs, low=mid+1, high=high, needle=needle)
        else:
            raise ValueError("this should never happen")
    return -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Two cases:
        # 1. Target exists in array.
        # 2. Target not present in array.
        # In case one:
        # a. Find target with binary search.
        # b. Move backwards (towards 0 index) until we find where the
        #    number changes. This is our starting index.
        # c. Move forwards (towards n index) until we find where the
        #    target changes. This is our ending index.
        # d. Return the indices found in steps b and c.
        # In case two:
        # If it's not present just return [-1, -1].
        n = len(nums)
        target_idx = binary_search(
            xs=nums, low=0, high=n-1, needle=target,
        )
        if target_idx == -1:
            return [-1, -1]

        start, end = target_idx, target_idx
        while start > -1 and nums[start] == target:
            start -= 1
        while end < n and nums[end] == target:
            end += 1
        return [start+1, end-1]
