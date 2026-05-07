class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
            r,c=len(grid),len(grid[0])
            res=0

            for i in range(r):
                for j in range(c):
                    if grid[i][j]!=1: continue
                    
                    tmp=4
                    if i>0:
                        if grid[i-1][j]==1: tmp-=1

                    if (i+1)<r:
                        if grid[i+1][j]==1: tmp-=1

                    if j>0:
                        if grid[i][j-1]==1: tmp-=1

                    if (j+1)<c:
                        if grid[i][j+1]==1: tmp-=1

                    res+=tmp

            return res