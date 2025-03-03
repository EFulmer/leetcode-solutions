import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Logic:
        # We can't calculate the shortest distance for every cell with
        # a single pass, since that single pass' answer may be
        # incorrect (a neighbor with unknown distance may turn out
        # be on the route to a shorter path to the nearest zero).
        # So, we make two passes, one starting from the top left cell
        # and a second starting from the bottom right.
        # This is in-place, but you could copy the matrix and set
        # cells that were 1 in the original matrix to math.inf or
        # some other sentinel value easily.
        m, n = len(mat), len(mat[0])

        for row in range(m):
            for col in range(n):
                # Skip any cell that's a known zero.
                if mat[row][col] > 0:
                    above = mat[row-1][col] if row > 0 else math.inf
                    left = mat[row][col-1] if col > 0 else math.inf
                    mat[row][col] = min(above, left) + 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                # Skip any cell that's a known zero.
                if mat[row][col] > 0:
                    below = mat[row+1][col] if row < m-1 else math.inf
                    right = mat[row][col+1] if col < n-1 else math.inf
                    # On our second pass, we may already have found a
                    # cell's absolute minimum, so we add that as a
                    # parameter to the call to min.
                    # That's also why we add 1 to the distances of
                    # below and right when we pass them as parameters
                    # to the min call.
                    mat[row][col] = min(mat[row][col], below + 1, right + 1)

        return mat
