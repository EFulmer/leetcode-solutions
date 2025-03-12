class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # General solution:
        # find where negatives end
        # then find where positives begin
        # return the max based on that
        # Short-circuit if everything is either positive or negative
        if nums[0] > 0 or nums[-1] < 0:
            return len(nums)
        last_negative_index = 0
        while last_negative_index < len(nums) and nums[last_negative_index] < 0:
            last_negative_index += 1

        first_positive_index = last_negative_index
        while first_positive_index < len(nums) and nums[first_positive_index] < 1:
            first_positive_index += 1

        positive_count = len(nums) - first_positive_index
        negative_count = last_negative_index
        return max(positive_count, negative_count)
