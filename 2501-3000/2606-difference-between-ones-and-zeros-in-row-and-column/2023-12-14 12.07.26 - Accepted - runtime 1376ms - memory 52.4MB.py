class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        ##### power by chatGPT #####

        # m, n = len(grid), len(grid[0])

        # ones_row = [0] * m
        # ones_col = [0] * n

        # for i in range(m):
        #     for j in range(n):
        #         ones_row[i] += grid[i][j]
        #         ones_col[j] += grid[i][j]

        # diff = [[0] * n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         diff[i][j] = ones_row[i] + ones_col[j] - grid[i][j] - (m - ones_row[i]) - (n - ones_col[j])

        # return diff

        m,n=len(grid[0]),len(grid)
        grid_t=list(zip(*grid))
        
        row0=[r.count(0) for r in grid]
        row1=[sum(r) for r in grid]
        col0=[c.count(0) for c in grid_t]
        col1=[sum(c) for c in grid_t]

        return [[row1[i]+col1[j]-row0[i]-col0[j] for j in range(m)] for i in range(n)]