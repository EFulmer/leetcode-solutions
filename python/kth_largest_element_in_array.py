import functools
import random


def partition(nums: List[int], left: int, right: int, pivot_index: int) -> int:
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # move pivot to end
    store_index = left
    for i in range(left, right):
        if nums[i] < pivot_value:
            nums[store_index], nums[i] = nums[i], nums[store_index]
            store_index += 1
    nums[right], nums[store_index] = nums[store_index], nums[right]
    return store_index


def select(nums: List[int], left: int, right: int, k: int) -> int:
    if left == right:
        return nums[left]
    select_ = functools.partial(select, nums=nums, k=k)
    pivot_index = random.randint(left, right)
    pivot_index = partition(nums=nums, left=left, right=right, pivot_index=pivot_index)
    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return select_(
            left=left, right=pivot_index-1,
        )
    else:
        return select_(
            left=pivot_index+1, right=right,
        )


def quick_select(nums: List[int], k: int) -> int:
    return select(nums, left=0, right=len(nums)-1, k=k)


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quick_select(nums=nums, k=len(nums)-k)
