class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == n:
            return n
        elif n == 0 or n == 1:
            return n
        winner = 1
        for i in range(1, n+1):
            subs = (
                sub for sub in n_wise(s, n=i)
                if len(sub) == len(set(sub))
            )
            try:
                next(subs)
                winner = i
            except:
                break
        return winner


n_wise = lambda g, n=2: zip(
    *(itertools.islice(g, i, None) for i, g in enumerate(itertools.tee(g, n)))
)
