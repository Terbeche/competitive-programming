class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows_numbers, columns_number  = len(mat), len(mat[0]) 
        result = []

        initial_dict = defaultdict(list)

        for row in range(rows_numbers):
            for col in range(columns_number):
                initial_dict[row + col].append(mat[row][col])
    
        for key, value in initial_dict.items():
            if key % 2 == 0:
                initial_dict[key].reverse()

            result += value

        return (result)
