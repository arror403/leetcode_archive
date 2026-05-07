class Solution:
    # helped by Copilot
    def numIslands(self, grid: List[List[str]]) -> int:
        r,c=len(grid),len(grid[0])
        res=0

        def dfs(i,j):
            if i<0 or j<0 or i>=r or j>=c or grid[i][j]!="1": return
            # mark as visited
            grid[i][j]=-1
            # check: up, down, left, right
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i+x, j+y)

        for i in range(r):
            for j in range(c):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1

        return res