class Solution:
    def minTimeToReach(self, moveTime):
        rows = len(moveTime)
        cols = len(moveTime[0])
        costs = [[float("+inf")] * cols for _ in range(rows)]
        visited = set()
        costs[0][0] = 0
        heap = []
        heapq.heappush(heap, Node(distance=0, row=0, col=0))

        while heap:
            current = heapq.heappop(heap)
            current_coordinates = (current.row, current.col)
            if current_coordinates in visited:
                continue
            visited.add(current_coordinates)
            for row, col in valid_neighbors(current_coordinates, moveTime):
                dist = max(costs[current.row][current.col], moveTime[row][col]) + 1
                if dist < costs[row][col]:
                    costs[row][col] = dist
                    heapq.heappush(heap, Node(distance=dist, row=row, col=col))

        return costs[-1][-1]


Node = collections.namedtuple("Node", ["distance", "row", "col"])


def valid_neighbors(pos, grid):
    row, col = pos
    if row > 0:
        yield (row-1, col)
    if col > 0:
        yield (row, col-1)
    if row < len(grid) - 1:
        yield (row+1, col)
    if col < len(grid[0]) - 1:
        yield (row, col+1)
