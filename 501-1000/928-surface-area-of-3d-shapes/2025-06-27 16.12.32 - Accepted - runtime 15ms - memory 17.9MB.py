class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n=len(grid)
        res=t=0

        for r in grid:
            for c in r:
                res+=c
                if c>0: t+=(c-1)
        res*=6
        t*=2

        for r in range(n):
            for c in range(n):
                if r+1<n:
                    t+=min(grid[r][c], grid[r+1][c])
                if r>0:
                    t+=min(grid[r][c], grid[r-1][c])
                if c+1<n:
                    t+=min(grid[r][c], grid[r][c+1])
                if c>0:
                    t+=min(grid[r][c], grid[r][c-1])


        return res-t