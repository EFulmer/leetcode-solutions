class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i = array 1 pointer, j = array 2 pointer
        i, j = 0, 0
        first_vacancy = m
        while i < m  and j < n:
            # if the item at the current spot in the second array
            # should be before the current, move everything in nums1
            # up one index, copy nums2[j] to nums1[i] then advance
            # j by one
            if nums1[i] > nums2[j]:
                for k in range(first_vacancy, i-1, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                first_vacancy += 1
                m += 1
                j += 1
            else:
                i += 1
        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
