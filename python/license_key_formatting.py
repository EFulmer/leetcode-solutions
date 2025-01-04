class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        intermediate = s.replace("-", "").upper()
        bucket_size = len(intermediate) // k
        acc = []
        # take k from the back, add them to result[i], move on
        end = len(intermediate)
        while end >= k:
            start = max(0, end-k)
            current = intermediate[start:end]
            acc.append(current)
            end = start
        if end != 0:
            acc.append(intermediate[:end])
        return "-".join(acc[::-1])
