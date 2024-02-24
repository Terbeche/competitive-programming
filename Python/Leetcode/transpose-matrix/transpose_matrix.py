class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows_numbers = len(matrix)
        columns_numbers = len(matrix[0])

        new_matrix = [[0 for _ in range(rows_numbers)] for _ in range(columns_numbers)]

        for row in range(rows_numbers):
            for col in range(columns_numbers):
                new_matrix[col][row] = matrix[row][col]

        return (new_matrix)
