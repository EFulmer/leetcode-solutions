class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        cols = len(grid)
        rows = len(grid[0])
        computers_by_col = [0 for _ in range(cols)]
        computers_by_row = [0 for _ in range(rows)]

        for col in range(cols):
            for row in range(rows):
                if grid[col][row] != 0:
                    computers_by_row[row] += 1
                    computers_by_col[col] += 1
        result = 0
        for col in range(cols):
            for row in range(rows):
                if grid[col][row] != 0 and (computers_by_row[row] > 1 or computers_by_col[col] > 1):
                    result += 1
        return result
