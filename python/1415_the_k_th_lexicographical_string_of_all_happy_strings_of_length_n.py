LETTERS = frozenset("abc")


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        hs = list(generate_happy_strings(n))
        hs.sort()
        try:
            return hs[k-1]
        except IndexError:
            return ""


def generate_happy_strings(n: int):
    if n < 0:
        raise ValueError("cannot generate strings of negative length")
    elif n == 0:
        yield ""
    elif n == 1:
        yield from "abc"
    else:
        for hs in generate_happy_strings(n-1):
            yield from (c + hs for c in LETTERS if c != hs[0])
