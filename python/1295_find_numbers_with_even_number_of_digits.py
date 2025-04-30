class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(
            1 for n in nums
            if number_of_digits(n) % 2 == 0
        )

def number_of_digits(x: int) -> int:
    return int(math.log10(x) + 1)
