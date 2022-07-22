class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1
        current_index = 0
        next_index = 1
        while next_index < len(nums):
            # check if current and next match
            if nums[current_index] == nums[next_index]:
                # nuke next if they do
                nums.pop(current_index)
            else:
                # if not, advance both and increment uniques
                current_index += 1
                next_index += 1
        return len(nums)
