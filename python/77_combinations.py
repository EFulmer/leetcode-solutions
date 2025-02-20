class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        gen = combinations(n, k)
        return list(gen)


def combinations(n, k):
    # Lifted and (barely) modified from Python's itertools module.
    # General idea:
    # First create a copy of the pool of items we can draw from,
    # which we simply call `pool`.
    pool = tuple(range(1, n+1))
    # Then, maintain a set of indices. Each combination is just the
    # items at the current values of indices, then we update indices to
    # point to the indices of the next permutation.
    indices = list(range(k))

    # First perm: items [1..k] (inclusive, as indicated by the square
    # brackets)
    yield tuple(pool[i] for i in indices)
    while True:
        # Update the indices for the next permutation:
        # The way we do this is shifting each value of indices up by
        # one for the next combination, which we do in the next
        # for-loop. Explaining here for an easily-readable,
        # top-to-bottom explainer.
        # Explaining the in words:
        # The decreasing for-loop here basically works as a check that
        # we can choose indices for our next permutation that are
        # within bounds, and find the lowest index in the set we can
        # increase.
        #
        # For instance, with n = 5 and k = 3, the first check of the
        # first iteration is indices[2] != 2 + 5 - 3,
        # simplifying to indices[2] != 4. 4 would be the last index.
        # If that's not the case, the next permutation is within our
        # ordered set of indices and is kosher. So we continue.
        # Continuing on to index 1 (counting backwards, remember),
        # then it checks that indices[1] != 5, which is beyond the
        # bounds of the indexed set of items to pick combinations from.
        # If any of those checks fail, we have a new permutation.
        # Otherwise we hit the `else` of the `for`...`else` loop and
        # have exhausted the permutations.
        # The indices are ordered, so indices[i] must be > indices[i-1]

        # Find the first index we can increase without going out of
        # bounds
        for i in reversed(range(k)):
            # Is i + n - k OOB?
            # If not, break.
            if indices[i] != i + n - k:
                break
        # If we can't increase any index without going OOG, we're done.
        else:
            return

        # At this point, index i is the smallest index that we can
        # increase. So increment its value.
        indices[i] += 1
        # Then, starting from the first index after i, set its value
        # to the prior one plus one.
        # So we end up getting something like:
        # (first yield, outside the loop → (0, 1, 2))
        # First yield inside the while loop → indices (0, 1, 3)
        # Second yield inside the while loop → indices (0, 1, 4)
        # then we've maxed out indices[2], so we start incrementing
        # indices[1] and get indices (0, 2, 3), ...
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
