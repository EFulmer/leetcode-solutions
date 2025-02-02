import itertools


pair_wise = lambda g: zip(
    *(itertools.islice(g, i, None)
    for i, g in enumerate(itertools.tee(g, 2)))
)


all_ascending = lambda xs: all(x <= y for x, y in pair_wise(xs))


def yield_starting_from(xs, i):
    """Yield all the elements of xs, starting from index i."""
    for j in range(n := len(xs)):
        yield xs[(i + j) % n]


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if all_ascending(yield_starting_from(nums, i)):
                return True
        return False
