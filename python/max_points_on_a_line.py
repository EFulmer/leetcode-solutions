from collections import Counter
import itertools


class Solution:

    sentinel = 1j

    def maxPoints(self, points: List[List[int]]) -> int:
        # Early termination:
        # You can construct a line between any two points in R^2,
        # and one point is trivial
        if len(points) < 3:
            return len(points)

        # Otherwise, we need to figure out:
        # for each "interesting" line you can construct (intersects at least 2 points),
        # how many points total lie on it?
        max_so_far = 0
        for i, point_1 in enumerate(points):
            x_1, y_1 = point_1
            lines_thru_p1 = Counter(
                self.find_slope(x_1, y_1, x_2, y_2)
                for x_2, y_2 in itertools.islice(points, i+1, None, None)
            )
            if len(lines_thru_p1) > 0:
                max_so_far = max(max_so_far, lines_thru_p1.most_common(1)[0][1])
        return max_so_far + 1

    def find_slope(self, x_1: int, y_1: int, x_2: int, y_2: int) -> int:
        # Rise over run!
        if x_1 == x_2:
            return self.sentinel
        return (y_1 - y_2) / (x_1 - x_2)
