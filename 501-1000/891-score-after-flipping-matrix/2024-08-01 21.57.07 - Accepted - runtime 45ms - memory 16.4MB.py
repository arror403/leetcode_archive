class Solution:
    def matrixScore(self, grid):
        r,c=len(grid),len(grid[0])
        res=0
        # Score from the first column
        res+=r*(1<<(c-1))
        # Score from the remaining columns
        for j in range(1,c):
            ones=sum(grid[i][j]==grid[i][0] for i in range(r))
            res+=max(ones, r-ones)*(1<<(c-j-1))
        
        return res