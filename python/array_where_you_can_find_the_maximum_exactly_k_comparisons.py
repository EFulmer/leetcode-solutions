LIMIT = 10 ** 9 + 7


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # We first need to handle the case where there's fewer numbers
        # than steps (since it's the exact number of steps)
        # n = length of array
        # m = max value allowed in array
        # k = number of comparisons (not a maximum)
        if m < k:
            return 0
        # This can be solved with dynamic programming, because the 
        # number of arrays of length n is dependent upon the number of
        # valid arrays of length n-1.
        # So we store a 2D array of the 
        # First, define the problem and the base cases:
        # Problem:
        # Need to find # of arrays, of length n, with values in range
        # [1, m] (so, inclusive) where finding the maximum element can
        # take EXACTLY k comparisons.
        # Base case:
        # 1 is the minimum number of comparisons you'll need.
        # ...
        # You need to find the number of comparisons for every number
        # up to n-1.
        # For each n:
        #   For i := k-1 .. 0:
        #       For j := 1 .. m:
        #           The number of arrays that satisfies the property
        #           with m == i and k == j is equal to:
        #           (j + 1) + (number of ways with i-1 and j, if i > 0)
        #           The reasoning is: when k (number of comparisons)
        #           > 0, you add one additional possible array for
        #           each additional comparison that's allowed.
        options = [[1] * m] + [[0] * m for _ in range(k - 1)]
        for _ in range(n - 1):
            for i in range(k - 1, -1, -1):
                acc = 0
                for j in range(m):
                    options[i][j] = (options[i][j] * (j + 1) + acc) % LIMIT
                    if i > 0:
                        acc = (acc + options[i - 1][j]) % LIMIT
        return sum(options[-1]) % LIMIT
