class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # k-length sliding windows
        # get the one with the fewest W's in it; the number of Ws
        # is our answer
        substrings = n_wise(blocks, k)
        return min(sum(c == "W" for c in substring) for substring in substrings)


def n_wise(it, n=2):
    return zip(
        *(itertools.islice(g, i, None) for i, g in enumerate(itertools.tee(it, n)))
    )
