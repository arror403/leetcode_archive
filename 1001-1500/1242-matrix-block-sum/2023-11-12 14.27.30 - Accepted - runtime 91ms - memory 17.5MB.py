class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        prefix_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = mat[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                r1, c1 = max(0, i-k), max(0, j-k)
                r2, c2 = min(rows, i+k+1), min(cols, j+k+1)
                row.append(prefix_sum[r2][c2] - prefix_sum[r2][c1] - prefix_sum[r1][c2] + prefix_sum[r1][c1])
            result.append(row)

        return result


    #     return [[sum(sum(x) for x in self.neighbors(mat,k,i+1,j+1))
    #             for j in range(len(mat[0]))] for i in range(len(mat))]


    # def neighbors(self, a, radius, row_number, column_number):
    #     return [[a[i][j] if i >= 0 and i<len(a) and j>=0 and j<len(a[0]) else 0
    #             for j in range(column_number-1-radius, column_number+radius)]
    #             for i in range(row_number-1-radius, row_number+radius)]