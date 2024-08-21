class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n) for _ in range(m)]
        dp[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                value = 0

                if row < m - 1:
                    value += dp[row + 1][col] 
                if col < n - 1:
                    value += dp[row][col + 1]

                dp[row][col] = max(value, 1)

        return dp[0][0]