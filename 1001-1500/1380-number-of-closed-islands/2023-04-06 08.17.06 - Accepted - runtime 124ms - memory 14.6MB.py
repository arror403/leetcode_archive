class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            res = True
            res &= dfs(i+1, j)
            res &= dfs(i-1, j)
            res &= dfs(i, j+1)
            res &= dfs(i, j-1)
            return res
        
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j):
                    res += 1
        return res