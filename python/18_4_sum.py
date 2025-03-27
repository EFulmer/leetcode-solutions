class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Extend 3-sum:
        # For each pair of numbers in nums,
        # run two other pointers, starting from the last index
        # and the second one's index + 1
        # and binary search for two numbers that add up to the target.
        nums.sort()
        results = set()
        for cand_index_1, cand_1 in enumerate(nums):
            for cand_index_2, cand_2 in enumerate(nums[cand_index_1+1:], start=cand_index_1+1):
                cand_index_3 = cand_index_2 + 1
                cand_index_4 = len(nums) - 1
                needle = target - (cand_1 + cand_2)
                while cand_index_3 < cand_index_4:
                    current = nums[cand_index_3] + nums[cand_index_4]
                    if current == needle:
                        results.add(
                            (nums[cand_index_1], nums[cand_index_2], nums[cand_index_3], nums[cand_index_4])
                        )
                        cand_index_3 += 1
                        cand_index_4 -= 1
                    elif nums[cand_index_3] + nums[cand_index_4] > needle:
                        cand_index_4 -= 1
                    else:
                        cand_index_3 += 1
        return list(results)
