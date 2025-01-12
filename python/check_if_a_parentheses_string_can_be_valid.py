class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # Error handling and short-circuiting on some easy cases
        N = len(s)

        # Should never happen:
        if N != len(locked):
            raise ValueError("expected s and locked to have the same length")
        # Odd-length paren strings can never be balanced:
        elif N % 2 != 0:
            return False
        # If no characters are locked whatsoever, then any even string
        # is balanced:
        elif all(char == '0' for char in locked):
            return True

        open_parens_count = 0
        # We can save on memory by keeping a count of unlocked chars
        # and iterating through the strings twice.
        avail_unlocked_count = 0

        for char, lock in zip(s, locked):
            # Greedy: we "use" any unlocked characters as soon as we
            # find them. Increment the count of unlocked characters and
            # flip it if we encounter an unbalanced closing paren.
            # The reason for this is essentially that it's a
            # "better situation" to have exhausted our unlocked chars
            # by the end than have unused ones.
            if lock == '0':
                avail_unlocked_count += 1
            elif char == '(':
                open_parens_count += 1
            elif char == ')':
                if open_parens_count >= 1:
                    open_parens_count -= 1
                elif avail_unlocked_count >= 1:
                    avail_unlocked_count -= 1
                else:
                    return False

        # Work from the back of the string to the front to double-check
        # our bookkeeping: this makes sure we don't use an unlocked
        # character in a place it is not allowed (i.e. hasn't shown up
        # yet)
        unpaired_opens_count = 0
        for i in range(N-1, -1, -1):
            # If we're at an unlocked character, we expend it to close
            # any possible unpaired open parentheses
            if locked[i] == '0':
                unpaired_opens_count -= 1
                avail_unlocked_count -= 1
            elif s[i] == '(':
                unpaired_opens_count += 1
                open_parens_count -= 1
            elif s[i] == ')':
                unpaired_opens_count -= 1

            # Working from the end of the string back to the start,
            # an unpairable open parenthesis is always a failure.
            if unpaired_opens_count > 0:
                return False

            # If we've exhausted all our unlocked characters
            # and have no unpaired open parens, we're good.
            if avail_unlocked_count == unpaired_opens_count == 0:
                break

        # If we have unpaired open parentheses after reaching the end
        # (or expending all unlocked characters)
        # then the string cannot be balanced.
        if open_parens_count > 0:
            return False
        return True
