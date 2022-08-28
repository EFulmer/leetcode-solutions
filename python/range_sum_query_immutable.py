# solution 1: compute the sum needed when calling `sumRange`
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# solution 2: compute the sums of [0..i] on construction
class NumArray:

    def __init__(self, nums: List[int]):
        # could make this more efficient with `nwise`
        self.nums = [0 for _ in range(len(nums))]
        self.nums[0] = nums[0]
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i-1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            raise ValueError(f"left bound {left} greater than right bound {right}")
        if left == 0:
            return self.nums[right]
        return self.nums[right] - self.nums[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
