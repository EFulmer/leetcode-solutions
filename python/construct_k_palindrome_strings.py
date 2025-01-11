class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        N = len(s)
        if k == N:
            return True
        elif k > N:
            return False
        # The trick is: if any letter appears an odd number of times,
        # then you can only include it in a palindrome sandwiched
        # between other letters, e.g. "dad".
        # So, by the pigeonhole principle, if there's <= k letters
        # that appear an odd number of times, we're good.
        hist = collections.Counter(s)
        letters_with_odd_appearances = 0
        for v in hist.values():
            if v % 2 != 0:
                letters_with_odd_appearances += 1
            if letters_with_odd_appearances > k:
                return False
        return letters_with_odd_appearances <= k
