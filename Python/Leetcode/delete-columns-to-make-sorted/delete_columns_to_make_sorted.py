class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        counter = 0

        rows_number, cols_number = len(strs), len(strs[0])
        
        for col in range(cols_number):
            word = ""
            for row in range(rows_number):
                word += strs[row][col]

            if word != "".join(sorted(word)):
                counter +=1

        return counter
