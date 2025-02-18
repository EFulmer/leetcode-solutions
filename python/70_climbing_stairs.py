class Solution:
    def climbStairs(self, n: int) -> int:
        # This is literally just the Fibonacci sequence:
        # Basically, the number of ways to climb n steps is equal to
        # the ways there are to climb n-1 steps plus the number of ways
        # to climb n-2 steps.
        if n == 1:
            return 1
        if n == 2:
            return 2

        # "default" to 1 for the 0-stair case to simplify our math
        a = 1
        b = 1
        c = a + b

        for i in range(2, n):
            a = b
            b = c
            c = a + b

        return c
