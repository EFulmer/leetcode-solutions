def permutations(xs):
    # Recursive, generator-based approach.
    # If the list `xs` is empty or has a single element, it has one
    # permutation, and that permutation is `xs` itself.
    if len(xs) <= 1:
        yield xs
        return
    # Otherwise: we can recurse on the permutations of the sublist
    # without xs[0], and for each of those (we know this
    # since each call makes a recursive call with a sublist one element
    # smaller)
    # and for each of those "partial permutations" (calling them
    # partial" because they don't have xs[0]), we can get a full
    # permutation by yielding the permutation with xs[0] at index i,
    # for every valid index i.
    for permutation in permutations(xs[1:]):
        for i in range(len(xs)):
            yield permutation[:i] + xs[0:1] + permutation[i:]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))
