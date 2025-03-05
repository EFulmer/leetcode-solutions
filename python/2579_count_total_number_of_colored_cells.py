class Solution:
    def coloredCells(self, n: int) -> int:
        # f(1) -> 1
        # f(2) -> 5
        # f(3) -> 13
        if n == 1:
            return 1
        elif n == 2:
            return 5
        a, b = 1, 5
        i = 2
        while i < n:
            a, b = b, (4 * i + b)
            i += 1
        return b
