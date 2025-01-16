from functools import cache

@cache
def is_pair_bad(c1: str, c2: str) -> bool:
    if len(c1) != 1:
        raise ValueError(f"Expected c1 to be a one-length string, got {c1}")
    if len(c2) != 1:
        raise ValueError(f"Expected c2 to be a one-length string, got {c2}")
    return c1 != c2 and c1.upper() == c2.upper()


@cache
def is_pair_good(c1: str, c2: str) -> bool:
    return not is_pair_bad(c1=c1, c2=c2)


class Solution:
    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s
        result = list(s)
        still_can_remove = True
        while still_can_remove:
            if len(result) < 2:
                break
            new_result = [result[0]]
            for i in range(1, len(result)):
                if len(new_result) == 0:
                    new_result.append(result[i])
                elif is_pair_good(new_result[-1], result[i]):
                    new_result.append(result[i])
                else:
                    new_result.pop()
            still_can_remove = len(new_result) != len(result)
            result = new_result
        result = "".join(result)
        return result
