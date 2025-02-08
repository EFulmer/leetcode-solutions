class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if (n := len(triangle)) == 1:
            return triangle[0][0]
        dp = [[0 for cell in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            m = len(triangle[i])
            for j in range(m):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == m-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])
