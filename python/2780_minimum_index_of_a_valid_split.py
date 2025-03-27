class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Strategy:
        # 1. Find the mode ("most dominant" element) - O(n)
        # 2. Iterate over the indices and keep track of how many times
        #    the mode appears in indices [0..i]. Once the mode of the
        #    whole array is the same as the mode of A[0..i], return i.
        # 3. TODO: how to figure out the failure case? I think it's if
        #    every occurrence of the mode appears in the first half of
        #    A.
        full_count = Counter(nums)
        mode, mode_count = full_count.most_common(1)[0]
        n = len(nums)
        running_count = Counter()
        for i in range(n-1):
            current_num = nums[i]
            full_count[current_num] -= 1
            running_count[current_num] += 1
            if current_num == mode and running_count[current_num] * 2 > i + 1 and full_count[current_num] * 2 > n - i - 1:
                    return i
        return -1
