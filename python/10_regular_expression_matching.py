class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Let's short-circuit on some easy cases, first:
        # 1. If the pattern is ".*", it matches everything.
        if p == ".*":
            return True
        # I think a pattern can be longer than a string it matches:
        # if the pattern is "ab*", it matches "a", and "ab".
        # ".*" may be the only short-circuit.
        # Regexes are actually NFAs, but this restricted
        # subset means that implementing it that way is prob. overkill
        def helper(str_ind: int, pat_ind: int) -> bool:
            if p[pat_ind:] == ".*":
                return True
            # If we've reached the end of the pattern, it matches iff
            # we've also reached the end of the string.
            elif pat_ind >= pat_len:
                return str_ind >= str_len

            current_letter_matches = str_ind < str_len and \
                p[pat_ind] in {".", s[str_ind]}
            # There are two "general" cases. Either we have a * or not.
            # If we have a *, then we have a "get out of jail free"
            # card if the rest matches, since the * accepts 0 matches.
            if pat_ind < pat_len - 1 and p[pat_ind+1] == "*":
                return (
                    # If it doesn't match, you only move forward in the
                    # pattern, but by 2 indices because there was no
                    # match for whatever letter got *'d.
                    helper(str_ind=str_ind, pat_ind=pat_ind+2)
                    # If it matches, move forward in the string, but
                    # not the pattern.
                    or current_letter_matches
                    and helper(str_ind=str_ind+1, pat_ind=pat_ind)
                )
            else:
                return current_letter_matches and \
                    helper(str_ind=str_ind+1, pat_ind=pat_ind+1)

        pat_len, str_len = len(p), len(s)
        return helper(str_ind=0, pat_ind=0)
