class Solution:
    def matrixScore(self, grid):
        m,n=len(grid),len(grid[0])
        # Step 1: Flip rows to ensure the first column is all 1s
        for i in range(m):
            if grid[i][0]==0:
                for j in range(n):
                    grid[i][j]=1-grid[i][j]
        # Step 2: Flip columns (except the first) if it increases the score
        for j in range(1,n):
            count=sum(grid[i][j] for i in range(m))
            if count<=(m//2):
                for i in range(m): grid[i][j]=1-grid[i][j]
        # Step 3: Calculate the final score
        return sum(int(''.join(map(str, row)), 2) for row in grid)