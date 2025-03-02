import itertools
from typing import List


# Solution 1: Not using groupby
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ids_1 = (n[0] for n in nums1)
        ids_2 = (n[0] for n in nums2)
        max_id = max(itertools.chain(ids_1, ids_2))
        results = [0] * (max_id + 1)
        for id_, val in nums1:
            results[id_] = val
        for id_, val in nums2:
            results[id_] += val
        final_result = [[i, result] for (i, result) in enumerate(results) if result != 0]
        return final_result


# Solution 2: Groupby (less performant, because Python's
# `itertools.groupby` looks for consecutive runs, not an "absolute"
# grouping like in SQL)
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        g = itertools.groupby(sorted(nums1 + nums2), key=lambda x: x[0])
        result_dict = {}
        for item in g:
            idx = item[0]
            vals = [i[1] for i in item[1]]
            result_dict[idx] = sum(vals)
        result_list = []
        for key, val in result_dict.items():
            result_list.append([key, val])
        return sorted(result_list, key=lambda x: x[0])
