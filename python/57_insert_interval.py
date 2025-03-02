class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        i = 0
        result = []
        # First, find all intervals that cleanly fit "before" the new
        # interval, and add them to our result.
        # (Creating a new array for the result uses more memory, but
        # simplifies our "bookkeeping.")
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Once we've found the first of the old intervals which the new
        # interval would "overlap," we merge those overlapping
        # intervals into a single interval.
        # We check that by seeing if the new interval ends after some
        # existing interval starts (already covered the new interval's
        # start point in the prior loop), and then we merge them by
        # "stretching" the new interval to encompass both it and any
        # overlapping intervals.
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # We can simply copy over the remaining intervals that
        # "come after" the new interval without any "overlap."
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
