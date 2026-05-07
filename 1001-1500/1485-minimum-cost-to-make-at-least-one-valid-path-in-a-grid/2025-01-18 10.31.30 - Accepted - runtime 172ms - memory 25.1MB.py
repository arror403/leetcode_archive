class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        cost = 0
        dp = [[10**9]*n for _ in range(m)]
        q = deque()
        self.dfs(grid, 0, 0, dp, cost, q)

        while q:
            cost+=1
            L = len(q)
            for i in range(L):
                r, c = q.popleft()
                for j in range(4):
                    self.dfs(grid, r + d[j][0], c + d[j][1], dp, cost, q)

        return dp[m - 1][n - 1]


    def dfs(self, grid, r, c, dp, cost, q):
        d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(grid), len(grid[0])
        if (r < 0 or r >= m or c < 0 or c >= n or dp[r][c] != 10**9): return

        dp[r][c] = cost
        q.append([r, c])
        nextDir = grid[r][c] - 1

        self.dfs(grid, r + d[nextDir][0], c + d[nextDir][1], dp, cost, q)