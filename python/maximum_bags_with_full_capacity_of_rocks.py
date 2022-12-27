class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        # Classified as a greedy problem, so
        # See how much remaining capacity each bag has:
        differences = [c - r for c, r in zip(capacity, rocks)]
        differences = sorted(differences)
        # Go through the bags with differences > 0:
        # place differences[i] rocks in each
        # until additionalRocks is 0
        # then return the # of indexes of differences where d[i] == 0
        for i in range(len(differences)):
            if additionalRocks == 0:
                break
            if differences[i] == 0:
                continue
            if additionalRocks >= differences[i]:
                additionalRocks -= differences[i]
                differences[i] = 0
        return len([d for d in differences if d == 0])
