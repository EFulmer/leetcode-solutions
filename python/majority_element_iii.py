from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        c = Counter(nums)
        return [k for k, v in c.items() if v > threshold]


# solution with O(1) space usage:

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # There can be at most two "tri-majority" elements since:
        # 1. if there were three, that'd be the entire array (all
        # elements are one of three values)
        # and 2. they're looking for MORE than floor(len(nums) / 3)
        result_1 = 0
        result_2 = 0
        count_1 = 0
        count_2 = 0

        threshold = len(nums) // 3

        for num in nums:
            if num == result_1:
                count_1 = count_1 + 1
            elif num == result_2:
                count_2 = count_2 + 1
            elif count_1 == 0:
                result_1 = num
                count_1 = 1
            elif count_2 == 0:
                result_2 = num
                count_2 = 1
            else:
                count_1 = count_1 - 1
                count_2 = count_2 - 1

        return {result for result in [result_1, result_2]
                if nums.count(result) > threshold}
