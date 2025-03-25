class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort them.
        intervals.sort()
        # Then go through the sorted array and merge any overlapping.
        i = 0
        while i < len(intervals) - 1:
            ci, ni = intervals[i], intervals[i+1]
            if ci[1] >= ni[0]:
                intervals[i] = [ci[0], max(ci[1], ni[1])]
                intervals.pop(i+1)
            else:
                i += 1
        return intervals
