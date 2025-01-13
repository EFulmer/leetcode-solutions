class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        hist = collections.Counter(s)
        done = False
        while not done:
            for k, v in hist.items():
                if v > 2:
                    hist[k] -= 2
            done = all(v < 3 for v in hist.values())
        return sum(hist.values())
