from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * (n) for _ in range(n)]

        for row in range(n - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                down = float('inf')
                down_right = float('inf')
                down_left = float('inf')
    
                if row == n -1:
                    dp[row][col] = matrix[row][col]
                    continue

                if row < n - 1:
                    down = dp[row + 1][col] 
                    if col < n - 1:
                        down_right = dp[row + 1][col + 1]
                    if col > 0:
                        down_left = dp[row + 1][col - 1]

                dp[row][col] = matrix[row][col] + min(down, down_right, down_left)

        return min(dp[0][:])