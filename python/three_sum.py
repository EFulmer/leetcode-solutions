class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = set()
        n = len(nums)
        for i, num in enumerate(nums):
            j = i + 1
            k = n - 1
            target = -num
            while j < k:
                current = nums[j] + nums[k]
                if current == target:
                    results.add((nums[i], nums[j], nums[k]))
                    j = j + 1
                    k = k - 1
                elif nums[j] + nums[k] > target:
                    k = k - 1
                else:
                    j = j + 1
        return results
