class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2
        else:
            acc = 1
            while n > 0:
                if n % 3 == 0:
                    acc *= 3
                    n -= 3
                else:
                    acc *= 2
                    n -= 2
            return acc
