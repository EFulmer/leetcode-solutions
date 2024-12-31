# opt(s, t, i, j): how many ways to form a subsequence of s[:i] using only characters from t[:j]
# opt(s, t, i, j) = { if i == j == 0 : 1
#                   { if i >= len(s) : opt(s, t, len(s), j)
#                   { if j >= len(t) : opt(s, t, i, len(t))
#                   { if i > j       : 0
#                   { if i <= j      : if s[i] == t[j] then 1 + opt(s, t, i-1) + opt else opt(s, t, i-1, j) + opt(s, t, i, j-1)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        s_ind = t_ind = 0

        while s_ind < len(s) and t_ind < len(t):
            if s[s_ind] == t[t_ind]:
                s_ind += 1
            t_ind += 1

        return s_ind == len(s)
