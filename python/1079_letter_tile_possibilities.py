import itertools


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # number of permutations of each length n, for every n between 1 and len(tiles)
        acc = 0
        for i in range(1, len(tiles)+1):
            acc += len(set(itertools.permutations(tiles, i)))
        return acc
