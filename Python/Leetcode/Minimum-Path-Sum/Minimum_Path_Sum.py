class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0] * (n) for _ in range(m)]

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                down = float('inf')
                right = float('inf')

                if row < m - 1:
                    down = dp[row + 1][col] 
                if col < n - 1:
                    right = dp[row][col + 1]

                if row == m -1 and col == n -1:
                    dp[row][col] = grid[m - 1][n -1]
                    continue

                dp[row][col] =  grid[row][col] + min(right, down)

        return dp[0][0]