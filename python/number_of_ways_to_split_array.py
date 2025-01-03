from itertools import accumulate


def prefix_sum(xs: list[int]) -> list[int]:
    return list(accumulate(xs))


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ps = prefix_sum(nums)
        total = ps[-1]
        result = 0
        for i in range(0, len(ps)-1):
            if ps[i] >= (total - ps[i]):
                result += 1
        return result
