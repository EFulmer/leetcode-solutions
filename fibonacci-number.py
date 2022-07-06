class Solution:
    cache = [0, 1]
    def fib(self, n: int) -> int:
        if n < len(self.cache):
            result = self.cache[n]
        else:
            result = sum(self.cache[-2:])
            self.cache.append(result)
        return result
