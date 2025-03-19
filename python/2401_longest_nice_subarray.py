class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        winner = 1
        for n in range(2, min(31, len(nums)+1)):
            windows = n_wise(nums, n)
            any_nice = any(is_nice(window) for window in windows)
            if any_nice:
                winner = n
            else:
                break
        return winner


def n_wise(it, n):
    return zip(
        *(itertools.islice(g, i, None)
        for i, g in enumerate(itertools.tee(it, n)))
    )


def is_nice(it):
    pairs = itertools.permutations(it, r=2)
    for p1, p2 in pairs:
        if p1 & p2 != 0:
            return False
    return True
