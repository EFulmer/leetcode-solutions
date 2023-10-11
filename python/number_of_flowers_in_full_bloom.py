from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(
            self, flowers: List[List[int]], people: List[int]
        ) -> List[int]:
        # The number of flowers that are in bloom on a specific date is
        # equal to the number that have blossomed at or before that
        # date, minus the number will wilt after that date.
        # Can't do binary search for this, since we want to know how
        # many flowers will have bloomed by that date and BS just gives
        # any old index where the value appears.
        # (or we could binary search, then check that it gets the last
        # index)
        # bisect_right and bisect_left are needed - right for the start
        # because that gets the index of the last bloom at or before
        # the person's visit date,
        # and left for the end because that gets the index of the
        # first wilt at or before the aforementioned date.
        starts = sorted(s for s, e in flowers)
        ends = sorted(e for s, e in flowers)
        return [
            bisect_right(starts, person) - bisect_left(ends, person)
            for person in people
        ]
