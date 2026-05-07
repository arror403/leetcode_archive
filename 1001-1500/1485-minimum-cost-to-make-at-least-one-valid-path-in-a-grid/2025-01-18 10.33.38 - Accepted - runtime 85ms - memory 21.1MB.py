class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dp = [[float('inf')] * n for _ in range(m)]
        q = deque()
        
        def dfs(r, c, cost):
            if r < 0 or r >= m or c < 0 or c >= n or dp[r][c] <= cost:
                return
            dp[r][c] = cost
            q.append((r, c))
            nr, nc = r + dirs[grid[r][c]-1][0], c + dirs[grid[r][c]-1][1]
            dfs(nr, nc, cost)
        
        dfs(0, 0, 0)
        cost = 0
        
        while q:
            cost += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dirs:
                    dfs(r + dr, c + dc, cost)
                    
        return dp[m-1][n-1]