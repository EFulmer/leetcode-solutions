class Solution(object):
    cache = [0, 1, 1, 2, 4]

    def _populate_cache(self, n: int):
        current_cache_size = len(self.cache)
        for i in range(current_cache_size, n):
            tri = sum(self.cache[-3:])
            self.cache.append(tri)

    def tribonacci(self, n: int) -> int:
        if n < len(self.cache):
            return self.cache[n]
        else:
            self._populate_cache(n+1)
            return self.cache[n]
