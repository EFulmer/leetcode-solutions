# The problem is actually asking: what's the largest
# (i.e. greatest area) rectangle we can draw using heights?
# To answer that, we up the index at whichever height is lower.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start_ind = 0
        end_ind = len(height) - 1
        current_max = area(height, start_ind, end_ind)
        while start_ind < end_ind:
            if height[start_ind] <= height[end_ind]:
                start_ind += 1
            else:
                end_ind -= 1
            current_max = max(
                current_max, area(height, start_ind, end_ind)
            )
        return current_max


def area(heights: List[int], start: int, end: int) -> int:
    return (end - start) * min(heights[start], heights[end])
