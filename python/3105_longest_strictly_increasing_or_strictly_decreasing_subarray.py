class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        decreasing_subsequences = [
            list(yield_while_decreasing(nums, i))
            for i in range(n)
        ]
        increasing_subsequences = [
            list(yield_while_increasing(nums, i))
            for i in range(n)
        ]
        longest_decreasing = max(len(s) for s in decreasing_subsequences)
        longest_increasing = max(len(s) for s in increasing_subsequences)
        return max(longest_decreasing, longest_increasing)


def yield_while_decreasing(xs, start):
    yield from yield_while(xs, start, operator.lt)


def yield_while_increasing(xs, start):
    yield from yield_while(xs, start, operator.gt)


def yield_while(xs, start, binop):
    current = xs[start]
    yield current
    for i in range(start+1, len(xs)):
        if binop(xs[i], current):
            current = xs[i]
            yield current
        else:
            return
