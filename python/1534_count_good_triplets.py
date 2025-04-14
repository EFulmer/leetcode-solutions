class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        all_triplets = itertools.combinations(arr, 3)
        result = 0
        for (t1, t2, t3) in all_triplets:
            if abs(t1 - t2) <= a and abs(t2 - t3) <= b and abs(t1 - t3) <= c:
                result += 1
        return result
