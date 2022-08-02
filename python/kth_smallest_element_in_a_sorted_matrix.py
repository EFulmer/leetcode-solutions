class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # binary search
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]

        while low < high:
            median = low + ((high - low) // 2)
            tmp = n - 1
            count_seen = 0

            # For each row:
            for i in range(0, n):
                # count elements smaller than the median in the current row, matrix[low:high][:]
                # (count downward)
                while tmp >= 0 and matrix[i][tmp] > median:
                    tmp = tmp - 1
                count_seen = count_seen + tmp + 1

            # if there's less than k elements smaller than the median,
            # shift the lower bound of the search range
            if count_seen < k:
                low = median + 1
            else: # shift the upper bound
                high = median
        return low
