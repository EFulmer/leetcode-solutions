class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        indices_to_delete = [False] * len(s)
        for i in range(n):
            if s[i].isdigit():
                indices_to_delete[i] = True
                j = i - 1
                while j > -1:
                    if not s[j].isdigit() and not indices_to_delete[j]:
                        indices_to_delete[j] = True
                        break
                    else:
                        j -= 1
        result = "".join(
            letter
            for (delete, letter) in zip(indices_to_delete, s)
            if not delete
        )
        return result
