from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # most_common returns a list of (number, count of occurrences) pairs
        return Counter(nums).most_common()[0][0]


# solution two:
