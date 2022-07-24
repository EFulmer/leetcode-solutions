class FirstSolution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # initialize the values
        row = column = 0
        # the length of each row is guaranteed to be the same, by the
        # problem definition
        m, n = len(matrix), len(matrix[0])
        # each row and column are sorted
        # going by rows:
        while row < m and column < n:
            # 1. if target > max(current_row) then go to the next row
            # 2. if min(current_row) <= target <= max(current_row)
            # then binary search?
            current_row = matrix[row]
            if target > max(current_row):
                row += 1
                continue
            else:
                for i in current_row:
                    if i == target:
                        return True
                row += 1
        return False

        # alt idea:
        # binary search rows, then binary search columns?
        # get rid of the rows it can't be in
        # then binary search the remaining columns
