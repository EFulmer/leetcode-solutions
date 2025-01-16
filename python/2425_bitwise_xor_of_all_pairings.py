from functools import reduce
from operator import xor


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Trick here:
        # for any number X, X ^ X == 0
        # So, let n := len(nums1) and m := len(nums2)
        # There's a property here which can be leveraged to avoid an
        # O(n * m) time and space cost.
        #
        # Let X be an arbitrary number in nums1.
        # And let Y be an arbitrary number in nums2.
        # If nums2 is of even length, X gets XOR'd an even number of
        # times (once with every Y in nums2) and cancels itself out.
        # And because X is an ARBITRARY number in nums2, this is true
        # for every X.
        # So, if nums2 is of even length, it's just the XOR of nums1.
        # Flip it for nums1 being even.
        # If both are of even length, then the result is 0.
        n = len(nums1)
        m = len(nums2)
        nums1_is_even = n % 2 == 0
        nums2_is_even = m % 2 == 0

        if nums1_is_even and nums2_is_even:
            return 0
        elif nums1_is_even and not nums2_is_even:
            return reduce(xor, nums1)
        elif nums2_is_even and nums1_is_even:
            return reduce(xor, nums1)
        else:
            result = 0
            for i in range(n):
                for j in range(m):
                    result = result ^ (nums1[i] ^ nums2[j])
            return result
