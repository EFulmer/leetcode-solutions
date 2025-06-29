MODULUS = 10**9 + 7


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Approach sketch:
        # We don't need a contiguous subsequence, so we can sort the
        # array.
        # A subsequence doesn't need to contain every item between i
        # and j, so what we need to do is find the index of the largest
        # item that satisfies the property, and then "work down,"
        # counting each subsequence in the range from 0 to the index of
        # the complement, from there.
        nums.sort()
        complement = target - nums[0]
        result = 0
        # All valid subsequences must be within this upper bound.
        j = find_approx_complement_index(nums, complement)
        i = 0
        while i <= j:
            # Now what remains is to check whether the current bounds
            # satisfy the condition:
            if nums[i] + nums[j] <= target:
                # If they do, there's 2 ** (bounds) valid subsequences
                # in the range: 2 for each item, since one includes it
                # and the other does not.
                subsequences_in_range = 2 ** (j - i)
                result += subsequences_in_range
                i += 1
            else:
                j -= 1
        return result % MODULUS

def find_approx_complement_index(nums, complement):
    """Find the highest index of `nums` containing `complement`.
    If `complement` is not in `nums`, return the index of the maximal
    (largest number smaller than `complement`) element in `nums`.
    """
    # Variant on binary search would be more efficient, but I haven't
    # finished my coffee yet.
    i = 0
    for i in range(len(nums)):
        if nums[i] > complement:
            break
    return i
