class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n) for _ in range(m)]
        dp[m - 1][n - 1] = 0

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                value = 0
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue

                if row < m - 1:
                    value += dp[row + 1][col]
                
                if col < n - 1:
                    value += dp[row][col + 1]
                if row != m - 1 or col != n - 1:
                    dp[row][col] = value
                else:
                    dp[row][col] = 1


        return dp[0][0]