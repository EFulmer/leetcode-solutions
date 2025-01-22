class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        return bfs_in_grid(isWater)


def bfs_in_grid(grid: list[list[int]]) -> list[list[int]]:
    m = len(grid)
    n = len(grid[0])
    result = [ [ float("-inf") for _ in range(n) ] for _ in range(m) ]

    # Start by initializing the "water" squares and adding them as
    # the squares to start from.
    queue = collections.deque()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result[i][j] = 0
                queue.append((i, j))

    # Track what "height" to give to the neighbors of the current queue-members:
    neighbor_height = 1

    while queue:
        neighbor_count = len(queue)
        next_neighbors = set()
        # For all the current squares, we know their height,
        # so we set their neighbors' heights to neighbor_height.
        for _ in range(neighbor_count):
            current_x, current_y = queue.popleft()
            for (neighbor_x, neighbor_y) in generate_neighbors(current_x, current_y, m, n):
                if result[neighbor_x][neighbor_y] == float("-inf"):
                    result[neighbor_x][neighbor_y] = neighbor_height
                    next_neighbors.add((neighbor_x, neighbor_y))

        queue.extend(next_neighbors)
        neighbor_height += 1
    return result


def generate_neighbors(x: int, y: int, m: int, n: int):
    neighbors = [ (x, y-1), (x, y+1), (x-1, y), (x+1, y) ]
    yield from [
        neighbor for neighbor in neighbors
        if is_valid(neighbor[0], neighbor[1], m, n)
    ]


def is_valid(x: int, y: int, m: int, n: int) -> bool:
    return 0 <= x < m and 0 <= y < n
