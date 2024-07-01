class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        for row in range(n):
            for col in range(m):
                if mat[row][col] == 1:
                    mat[row][col] = float('inf')

        for row in range(n):
            for col in range(m):
                if row > 0:
                    mat[row][col] = min(mat[row][col], mat[row - 1][col] + 1)
                if col > 0:
                    mat[row][col] = min(mat[row][col], mat[row][col - 1] + 1)

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if row < n - 1:
                    mat[row][col] = min(mat[row][col], mat[row + 1][col] + 1)
                if col < m - 1:
                    mat[row][col] = min(mat[row][col], mat[row][col + 1] + 1)

        return mat
