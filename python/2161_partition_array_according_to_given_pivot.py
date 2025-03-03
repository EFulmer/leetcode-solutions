class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_count = 0
        less_than = deque()
        greater_than = deque()
        for num in nums:
            if num == pivot:
                pivot_count += 1
            elif num < pivot:
                less_than.append(num)
            else:  # num > pivot
                greater_than.append(num)
        result = [None] * len(nums)
        i = 0
        while len(less_than) > 0:
            result[i] = less_than.popleft()
            i += 1
        while pivot_count > 0:
            result[i] = pivot
            pivot_count -= 1
            i += 1
        while len(greater_than) > 0:
            result[i] = greater_than.popleft()
            i += 1
        return result
