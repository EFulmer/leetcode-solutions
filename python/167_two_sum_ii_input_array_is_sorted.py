class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # For each item: search if its additive complement with the
        # target (in other words, `target - numbers[i]` for any valid
        # index `i`) is also in the array.
        # Another, more performant method would be to do the
        # "two pointers" strategy, starting one pointer at each end
        # of the array. If the sum of the values at the pointers
        # is smaller than the target, move the left pointer. If it's
        # greater, move the right pointer
        n = len(numbers)
        for i in range(n-1):
            needle = target - numbers[i]
            needle_index = binary_search(numbers, i+1, n-1, needle)
            if needle_index != -1:
                return [i+1, needle_index+1]


def binary_search(ns: list[int], low: int, high: int, target: int) -> int:
    while low <= high:
        mid = (low + high) // 2
        if ns[mid] == target:
            return mid
        elif ns[mid] < target:  # move into half w/ larger items
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Second solution:
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) - 1
        while left_index < right_index:
            current_sum = numbers[left_index] + numbers[right_index]
            if current_sum == target:
                return [left_index+1, right_index+1]
            elif current_sum < target:  # move the smaller pointer up
                left_index += 1
            else:
                right_index -= 1
