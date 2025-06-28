import operator
from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # If order was unimportant, you could just use a heap.
        # Keeping track of the original index of every item, first sort
        # nums by value, grab the biggest k, then re-sort those k by
        # original index, and return them.
        top_k = sorted(enumerate(nums), key=operator.itemgetter(1), reverse=True)[:k]
        top_k_by_index = sorted(top_k, key=operator.itemgetter(0))
        result = [num for index, num in top_k_by_index]
        return result
