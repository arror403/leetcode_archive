class Solution:
    def numRollsToTarget(self, n: int, k: int, x: int) -> int:
        # Initialize a 2D array to store the results
        dp=[[0]*(x+1) for _ in range(n+1)]

        # Base case: there is one way to get a sum of 0 with 0 dice
        dp[0][0]=1

        # Fill in the table using the recurrence relation
        for i in range(1,n+1):
            for j in range(1,x+1):
                for k_val in range(1,min(k,j)+1):
                    dp[i][j] = (dp[i][j]+dp[i-1][j-k_val]) % (10**9+7)

        # The answer is stored in dp[n][x]
        return dp[n][x]%(10**9+7)