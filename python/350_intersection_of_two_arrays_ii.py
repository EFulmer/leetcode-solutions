class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1_counts = collections.Counter(nums1)
        n2_counts = collections.Counter(nums2)
        final_counter = n1_counts & n2_counts
        final_result = []
        for k in final_counter:
            for i in range(final_counter[k]):
                final_result.append(k)
        return final_result
