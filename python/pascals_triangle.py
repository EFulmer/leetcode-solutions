class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1] * (r+1) for r in range(numRows)]
        for i in range(2, numRows):
            current_row = result[i]
            previous_row = result[i-1]
            for j in range(1, len(current_row)-1):
                current_row[j] = previous_row[j] + previous_row[j-1]
        return result
