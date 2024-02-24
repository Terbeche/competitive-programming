class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        rows_number = len(img)
        columns_number = len(img[0])

        result = [[0 for _ in range(columns_number)] for _ in range(rows_number)]

        for row in range(0, rows_number):
            for column in range(0, columns_number):

                cells_sum = 0
                cells_count = 0
                
                for i in range(max(0, row - 1), min(rows_number, row + 2)):
                    for j in range(max(0, column - 1), min(columns_number, column + 2)):
                            cells_sum += img[i][j]
                            cells_count += 1

                result[row][column] = cells_sum // cells_count

        return result
