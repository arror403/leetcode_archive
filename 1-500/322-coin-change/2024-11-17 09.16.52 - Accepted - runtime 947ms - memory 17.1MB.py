class Solution:
    def coinChange(self, coins: List[int], n: int) -> int:
        n+=1
        dp=[1]*n
        dp[0]=0
        coins.sort()

        for i in range(1,n):
            dp[i]=inf
            for c in coins:
                if (i-c)<0: 
                    break
                if dp[i-c]!=inf: 
                    dp[i]=min(dp[i], 1+dp[i-c])
 

        return -1 if dp[n-1]==inf else dp[n-1]