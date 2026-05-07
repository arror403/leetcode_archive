class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])

        # mark the rows and columns that contain zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
                    
        # set entire rows and columns to zero
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0