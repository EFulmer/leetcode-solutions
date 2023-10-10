# Approach one: naive
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


# Approach 2: use two modified binary searches:
def binary_search_start_of_range(xs: List[int], needle: int) -> int:
    # This is a modified binary search to find the first occurrence
    # of `needle` in `xs`.
    # (`needle` because of the phrase "needle in a haystack")
    # The difference between this and regular BS is that if we find
    # the `needle`, we don't immediately terminate. We set that
    # index-1 to the new upper bound, track the index, and keep
    # searching.
    low = 0
    high = len(xs) - 1
    index = -1
    mid = low + (high - low) // 2
    while low <= high:
        if xs[mid] > needle:
            high = mid - 1
        elif xs[mid] == needle:
            high = mid - 1
            index = mid
        else:
            low = mid + 1
        mid = low + (high - low) // 2
    return index


def binary_search_end_of_range(xs: List[int], needle: int) -> int:
    # This is a modified binary search to find the last occurrence
    # of `needle` in `xs`.
    # (`needle` because of the phrase "needle in a haystack")
    # The difference between this and regular BS is that if we find
    # the `needle`, we don't immediately terminate. We set that
    # index+1 to the new LOWER bound, track the index, and keep
    # searching.
    low = 0
    high = len(xs) - 1
    index = -1
    mid = low + (high - low) // 2
    while low <= high:
        if xs[mid] > needle:
            high = mid - 1
        elif xs[mid] == needle:
            low = mid + 1
            index = mid
        else:
            low = mid + 1
        mid = low + (high - low) // 2
    return index


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_idx = binary_search_start_of_range(xs=nums, needle=target)
        if start_idx == -1:
            return [-1, -1]
        else:
            return [
                start_idx, binary_search_end_of_range(xs=nums, needle=target)
            ]
