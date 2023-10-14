from functools import reduce
from operator import xor


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Naïve (directly compute all i^j pairs for i in nums1 and j in
        # nums2) is too slow but we can take advantage of something.
        # Specifically: x^x == 0 for every x
        # so if we reduce each array against ITSELF (a 2n operation)
        # and then figure out if that zeros out by checking whether the
        # other array's length is even or odd, we can  "compress" the
        # info down such that you don't nave to do the m*n operation of
        # computing the exclusive or of each pair.
        return (len(nums2) % 2 * reduce(xor, nums1, 0)) \
            ^ (len(nums1) % 2) * reduce(xor, nums2, 0)
