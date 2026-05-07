class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        ##### power by chatGPT #####

        rows, cols = len(mat), len(mat[0])
        row_count = [0] * rows
        col_count = [0] * cols
        special_count = 0

        # Count the number of 1s in each row and column
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Check each position in the matrix
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    special_count += 1

        return special_count