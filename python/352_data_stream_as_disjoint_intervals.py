class SummaryRanges:

    def __init__(self):
        # NOTE: A sorted set would be better here
        self.vals = []

    def addNum(self, value: int) -> None:
        if value not in self.vals:
            self.vals.append(value)

    def getIntervals(self) -> List[List[int]]:
        # Since getIntervals will be called less frequently than
        # addNum, sorting the values in getIntervals calls seems
        # to make sense to me.
        self._reindex()
        return list(self._yield_intervals())

    def _reindex(self):
        # Putting this call to the builtin list.sort method behind
        # another method in case we want to alter the internal
        # representation
        self.vals.sort()

    def _yield_intervals(self):
        idx = 0
        while idx < len(self.vals):
            idx, interval = self._build_current_interval(idx)
            yield interval

    def _build_current_interval(self, idx):
        # Get the interval starting at the current internal index.
        # basically, keep advancing through the internal array
        # as long as [idx, idx+1] are consecutive nonnegative ints.
        # then return the index that the next array starts at and
        # the current interval.
        start = self.vals[idx]
        ni = idx + 1
        while ni < len(self.vals):
            if self.vals[ni] == self.vals[idx] + 1:
                idx += 1
                ni += 1
            else:
                break
        return ni, [start, self.vals[idx]]

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
