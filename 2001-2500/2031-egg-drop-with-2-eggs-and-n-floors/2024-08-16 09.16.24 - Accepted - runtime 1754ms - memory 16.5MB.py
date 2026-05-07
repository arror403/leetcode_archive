class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp=[0]*(n+1)
        
        for i in range(1, n+1):
            dp[i]=inf
            for j in range(1, i+1):
                dp[i]=min(dp[i], 1+max(j-1, dp[i-j]))
        
        
        return dp[n]

        # return min((1+max(i-1, self.twoEggDrop(n-i)) for i in range (1,n)), default=1)