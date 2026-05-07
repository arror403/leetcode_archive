class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9+7
        maxPosition = min(steps//2, arrLen-1)
        
        # Create a 2D array to store the number of ways to reach each position at each step
        dp = [[0] * (maxPosition+1) for _ in range(steps+1)]
        
        # Initialize the base cases
        dp[0][0] = 1
        
        # Dynamic programming to fill in the dp array
        for i in range(1, steps+1):
            for j in range(maxPosition+1):
                dp[i][j] = dp[i-1][j]
                if j > 0:
                    dp[i][j] = (dp[i][j]+dp[i-1][j-1])%MOD
                if j < maxPosition:
                    dp[i][j] = (dp[i][j]+dp[i-1][j+1])%MOD
        
        return dp[steps][0]