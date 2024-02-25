class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        
        rows_number, cols_number = len(grid), len(grid[0])
        max_hourglass = 0

        for row in range(1, rows_number - 1):
            for col in range(1, cols_number - 1):
                potential_max = 0
                for i in range(max(0,row - 1), min(rows_number, row + 2)):
                    for j in range(max(0, col - 1), min(cols_number, col + 2)):
     
                        if (j == col - 1 and i == row) or (j == col + 1 and i == row):
                            continue
                        else:
                            potential_max += grid[i][j]
                max_hourglass = max(max_hourglass, potential_max)

        return max_hourglass
