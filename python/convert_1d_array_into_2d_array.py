class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Following m, n, o, ... convention for dimensions of matrices:
        o = len(original)
        if m * n != o:
            return []
        matrix = []
        # take n, advance pointer by n, continue
        current_row_start = 0
        current_row_end = n
        while current_row_end <= o:
            current_row = original[current_row_start:current_row_end]
            matrix.append(current_row)
            current_row_start += n
            current_row_end   += n
        return matrix
