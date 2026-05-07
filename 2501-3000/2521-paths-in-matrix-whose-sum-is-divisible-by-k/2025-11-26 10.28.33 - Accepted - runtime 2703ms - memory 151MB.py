class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-1]*(k+1) for _ in range(n+1)] for _ in range(m+1)]

        def dfs(i, j, s):
            if i == m or j == n: 
                return 0
            if i == m-1 and j == n-1: 
                return 0 if (s+grid[i][j])%k else 1 
            if dp[i][j][s] != -1: 
                return dp[i][j][s]
            dp[i][j][s] = (dfs(i+1, j, (s+grid[i][j])%k) + 
                           dfs(i, j+1, (s+grid[i][j])%k)) % (10**9 + 7)

            return dp[i][j][s]


        return dfs(0, 0, 0)