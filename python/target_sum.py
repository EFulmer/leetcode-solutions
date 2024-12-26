class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # naive solution: enumerate all possibilities
        current_sums = [0]
        for i, n in enumerate(nums):
            choices = [n, -n]
            new_sums = [
                s + choice
                for choice in choices
                for s in current_sums
            ]
            current_sums = new_sums
        return current_sums.count(target)
