from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        upper_bound = len(nums) - 1
        lower_bound = 0
        current_index = (upper_bound + lower_bound) // 2
        while upper_bound >= lower_bound:
            current_value = nums[current_index]
            if current_value == target:
                return current_index
            elif current_value > target:  # go lower
                upper_bound = current_index - 1
            elif current_value < target:  # go higher
                lower_bound = current_index + 1
            current_index = (upper_bound + lower_bound) // 2
        return -1
