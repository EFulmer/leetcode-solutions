class Solution:
    def isThree(self, n: int) -> bool:
        if n < 4:
            return False
        divisors = 2  # count 1, and n itself
        # +1 to include n // 2.
        upper_bound = (n // 2) + 1
        for i in range(2, upper_bound):
            if divisors > 3:
                return False
            divisors += n % i == 0
        return divisors == 3
