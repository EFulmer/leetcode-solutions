class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting algorithm:
        # Keep track of the majority element, initially assuming it's
        # the first item in the array, and keep a counter for every
        # appearance of it.
        # If that counter hits 0, then the current item is the new
        # candidate majority element.
        maj = float("-inf")
        count = 0

        for num in nums:
            if count == 0:
                maj = num
            if num == maj:
                count += 1
            else:
                count -= 1

        return maj
