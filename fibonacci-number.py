# to abstract it out, we need:
# last N to sum to get the next in the sequence
# the first N to start the sequence
# could write a generator and wrap it in the class...

def pump_gen(g):
    def f():
        g.send(None)
        yield from g
    return f()


# TODO: get pump/prime working
def n_o_nacci(cache: list, m: int):
    n = 0
    while True:
        if n < len(cache):
            n = yield cache[n]
        else:
            cache_length = len(cache)
            for i in range(cache_length, n+1):
                cache.append(sum(cache[-m:]))
            n = yield cache[n]


class Solution:

    @staticmethod
    def _cache(n):
        c = n_o_nacci([0, 1], 2)
        c.send(None)
        return c.send(n)

    def fib(self, n: int) -> int:
        return self._cache(n)
