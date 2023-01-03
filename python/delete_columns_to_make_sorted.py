class Solution:
    @staticmethod
    def is_sorted(s) -> bool:
        return all(s[i] <= s[i+1] for i in range(len(s)-1))

    def minDeletionSize(self, strs: List[str]) -> int:
        transposed = ["".join(s) for s in zip(*strs)]
        sorted = [t for t in transposed if self.is_sorted(t)]
        return len(transposed) - len(sorted)
