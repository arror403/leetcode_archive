class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # for (int i = 0; i < matrix.length - 1; i++)
        for i in range(len(matrix)-1):
            # for (int j = 0; j < matrix[i].length - 1; j++)
            for j in range(len(matrix[i])-1):
                if (matrix[i][j] != matrix[i+1][j+1]) :
                    return False
        return True
