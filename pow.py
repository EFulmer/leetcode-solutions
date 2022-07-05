def exponentiate(x: float, n: int) -> float:
    # special case n == 0 and n == 1 for speed
    if n == 0:
        return 1
    if n == 1:
        return x

    if n < 0:
        x = 1 / x
        n = -n

    res = 1
    while n > 0:
        if n % 2 == 0:
            # double x for each time we halve the number of iterations
            x = x * x
            n = n // 2
        else:
            res = res * x
            n = n - 1
    return res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return exponentiate(x, n)
