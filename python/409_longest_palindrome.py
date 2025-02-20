from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        # General algorithm idea:
        # 1. Create a counter of characters
        # With that counter...
        # 2. Take one of any odd-numbered character, that's your
        #    central letter for the palindrome. Decrement.
        # Continuing...
        # 3. For every letter that has 2 or more: append one instance of each letter on each side.
        # ...
        # Return length?
        # Alternate formulation:
        # start by counting each letter (counter structure or 52-index array)
        # take an odd-numbered item, +1 to the result (starts @ 0) for it
        # then keep sweeping through the counter till you can't anymore (elucidate)
        # if there's a letter with >=2 appearances, +2 to the result
        # repeat until you can't
        # return the result
        letter_counts = Counter(s)
        result = 0
        single_letter_used = False
        while counter_not_exhausted(letter_counts, single_letter_used):
            for (letter, count) in letter_counts.items():
                # When we have a letter that appears an even number of
                # times, we can always take half of the occurrences
                # and put it on the left side of the palindrome,
                # and put the other half on the right hand side.
                if count % 2 == 0:
                    result += count
                    letter_counts[letter] = 0
                # If a letter appears an odd number of times but more
                # than once, we can do the same thing except we have
                # one occurrence of it left over.
                elif count % 2 == 1 and count != 1:
                    result += count - 1
                    letter_counts[letter] = 1
                # If a letter appears once, we can put it at the center.
                # But we can only do this once.
                elif count == 1 and not single_letter_used:
                    result += 1
                    letter_counts[letter] = 0
                    single_letter_used = True
        return result


def counter_not_exhausted(
    letter_counts: Counter, single_letter_used: bool
) -> bool:
    """Return whether the letter counter has been exhausted.
    """
    # If the single letter rule has been used, we need to have some
    # remaining letters that appear at least twice.
    # Otherwise, if it hasn't been used, we can continue as long as
    # there are any letters remaining whatsoever.
    if single_letter_used:
        return any(v >= 2 for (_, v) in letter_counts.items())
    else:
        return any(v > 0 for (_, v) in letter_counts.items())
