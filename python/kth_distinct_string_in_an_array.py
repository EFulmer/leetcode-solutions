class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = {}
        for s in arr:
            counts[s] = counts.get(s, 0) + 1
        distinct = 0
        for s, v in counts.items():
            if v == 1:
                distinct += 1
            if distinct == k:
                return s

        return ""
