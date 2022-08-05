class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1[:]
        for n in nums2:
            midpoint = len(merged) // 2
            merged.insert(midpoint, n)
            merged.sort()
        midpoint = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[midpoint] + merged[midpoint-1]) / 2
        else:
            return merged[midpoint]
