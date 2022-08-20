class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = {n for n in nums if n > 0}
        if not numbers:
            return 1
        max_ = max(numbers)
        result = 1
        for i in range(1, max_+2):
            if i not in numbers:
                return i
        return result + 1
