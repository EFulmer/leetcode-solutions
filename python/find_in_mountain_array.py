# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


def find_peak(mountain_arr: 'MountainArray') -> int:
    # We can cut out a comparison (rather than grabbing 3 in a row then doing x < y < z, x < y > z, and x > y > z
    # if we just exclude the ending indices
    # since array[0] < array[1] and array > array by the property we're given
    low = 1
    high = mountain_arr.length() - 2
    while low != high:
        mid = low + (high - low) // 2
        candidate = mountain_arr.get(mid)
        next_above = mountain_arr.get(mid+1)
        # If we're on the ascent:
        if candidate < next_above:
            low = mid + 1
        else:
            high = mid
    return low

def binary_search_upslope(target, mountain_arr, low, high):
    while low <= high:
        mid = (high + low) // 2
        candidate = mountain_arr.get(mid)
        if candidate == target:
            return mid
        elif candidate > target:  # need to move `high` down
            high = mid - 1
        else:  # candidate < target, need to move `low` up
            low = mid + 1
    return -1


def binary_search_downslope(target, mountain_arr, low, high):
    while low <= high:
        mid = (high + low) // 2
        candidate = mountain_arr.get(mid)
        if candidate == target:
            return mid
        elif candidate > target:  # need to move lower bound up in this case
            low = mid + 1
        else:
            high = mid - 1
    return -1


def find_in_mountain_array(target, mountain_arr):
    # So first, I think you want to find the "peak"?
    # Then find which side of the peak the target is on
    # (hint says this requires two more searches)
    peak_index = find_peak(mountain_arr)
    peak_value = mountain_arr.get(peak_index)
    if target == peak_value:
        return peak_index
    if target > peak_value:
        return -1
    # Now we have a guarantee that there's two sorted sub-arrays,
    # and that means that we can use binary search on each of those
    # to find the index.
    # If it exists in both subarrays, we return the smaller index.
    # If neither we return -1.
    lower_index = binary_search_upslope(
        target, mountain_arr, 0, peak_index,
    )
    if lower_index != -1:
        return lower_index
    higher_index = binary_search_downslope(
        target, mountain_arr, peak_index+1, mountain_arr.length()-1,
    )
    return higher_index


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        return find_in_mountain_array(target, mountain_arr)
