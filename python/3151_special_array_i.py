import itertools

n_wise = lambda g, n=2: zip(
    *(itertools.islice(g, i, None) for i, g in enumerate(itertools.tee(g, n)))
)

diff_parity = lambda x, y: (x % 2) != (y % 2)

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all(diff_parity(x, y) for x, y in n_wise(nums))
