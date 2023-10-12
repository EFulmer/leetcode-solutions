class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_good = [check_row(board, i) for i in range(9)]
        columns_good = [check_column(board, i) for i in range(9)]
        subregions_good = [check_subregion(board, i, j) for i in range(3) for j in range(3)]
        return all(rows_good) and all(columns_good) and all(subregions_good)

def check_row(board, row: int) -> bool:
    all_digits = set('123456789')
    digits_in_row = [c for c in board[row] if c != '.']
    for digit in digits_in_row:
        try:
            all_digits.remove(digit)
        except KeyError:
            return False
    return True


def check_column(board, column: int) -> bool:
    all_digits = set('123456789')
    digits_in_column = [c for c in get_column(board, column) if c != '.']
    for digit in digits_in_column:
        try:
            all_digits.remove(digit)
        except KeyError:
            return False
    return True


def check_subregion(board, i, j):
    all_digits = set('123456789')
    digits_in_subregion = [
        d for d in get_subregion(board, i, j)
        if d != '.'
    ]
    for digit in digits_in_subregion:
        try:
            all_digits.remove(digit)
        except KeyError:
            return False
    return True


def get_column(board, column):
    return [board[i][column] for i in range(9)]

def get_subregion(board, i, j):
    if i < 0 or j < 0 or i > 2 or j > 2:
        raise ValueError(f"i and j should be in [0, 2], got {i, j = }")
    row_start = i * 3
    row_end = row_start + 3
    col_start = j * 3
    col_end = col_start + 3
    rows = board[row_start:row_end]
    subregion = [
        row[col_start:col_end]
        for row in board[row_start:row_end]
    ]
    flattened_subregion = [
        r for row in subregion for r in row
    ]
    return flattened_subregion
