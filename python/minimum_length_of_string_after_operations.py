class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) < 3:
            return len(s)
        hist = collections.Counter(s)
        # Repeatedly subtracting 2 occurrences of a character will
        # either result in its final count being 2
        # (when original count is even)
        # or 1 (when its original count is odd)
        # We can skip the "steps" using this fact.
        for k, v in hist.items():
            if v > 2:
                if v % 2 == 0:
                    hist[k] = 2
                else:
                    hist[k] = 1
        return sum(hist.values())
