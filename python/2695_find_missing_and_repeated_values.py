class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        items = [0] * (len(grid) ** 2 + 1)
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                current = grid[row][col]
                if items[current] == 1:
                    duplicate = current
                else:
                    items[current] = 1
        for index, item in enumerate(items):
            if item == 0:
                missing = index
        return [duplicate, missing]


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Reasoning:
        # We can make a system of two equations to solve for a and b (duplicate and missing).
        # a - b == difference between actual and expected
        # a ** 2 - b ** 2 == difference between squared sums
        # Expand and solve for a and b.
        n = len(grid)

        expected_sum = sum_of_first_n(n**2)
        actual_sum = sum_of_matrix(grid)

        expected_sum_of_squares = sum_of_first_n_squares(n**2)
        actual_sum_of_squares = sum_of_matrix_squared(grid)

        diff_of_sums = actual_sum - expected_sum
        diff_of_sums_of_squares = actual_sum_of_squares - expected_sum_of_squares

        a_plus_b = diff_of_sums_of_squares // diff_of_sums

        a = (a_plus_b + diff_of_sums) // 2
        b = (a_plus_b - diff_of_sums) // 2

        duplicate = a
        missing = b
        return [duplicate, missing]


@functools.cache
def sum_of_first_n(n: int) -> int:
    return (n * (n + 1)) // 2


@functools.cache
def sum_of_first_n_squares(n: int) -> int:
    return (n * (n + 1) * (2 * n + 1)) // 6


def sum_of_matrix(matrix: list[list[int]]) -> int:
    return sum(sum(cell for cell in row) for row in matrix)
