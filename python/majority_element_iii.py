from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        c = Counter(nums)
        return [k for k, v in c.items() if v > threshold]
