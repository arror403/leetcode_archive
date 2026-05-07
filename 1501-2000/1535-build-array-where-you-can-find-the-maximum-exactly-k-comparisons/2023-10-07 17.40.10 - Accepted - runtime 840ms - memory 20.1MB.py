class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD=10**9+7

        # Create a 3D DP array to store the results
        dp=[[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        
        # Initialize the DP array for n = 1
        for j in range(1, m+1):
            dp[1][j][1]=1
        
        # Fill the DP array
        for i in range(2, n+1):
            for j in range(1, m+1):
                for x in range(1, k+1):
                    dp[i][j][x] = (j*dp[i-1][j][x]+sum(dp[i-1][p][x-1] for p in range(1, j)))%MOD
        
        # Sum up the results for the last row (n = n) and return
        
        return sum(dp[n][j][k] for j in range(1, m+1))%MOD