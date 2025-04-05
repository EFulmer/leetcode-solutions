class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = lambda xs: functools.reduce(operator.__xor__, xs, 0)
        return sum(
            xor(permutation) for i in range(1, len(nums)+1)
            for permutation in itertools.combinations(nums, i)
        )
