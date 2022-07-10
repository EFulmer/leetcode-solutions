class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        # zip(strs) would zip each string;
        # [("flower", "flow")]
        # *strs turns it into a list of lists of strings;
        # e.g. (["f", "l", "o", "w", "e", "r"], ["f", "l", "o", "w"],)
        for c in zip(*strs):
            all_eq = all(x == c[0] for x in c)
            if all_eq:
                prefix.append(c[0])
            else:
                break
        return "".join(prefix)
