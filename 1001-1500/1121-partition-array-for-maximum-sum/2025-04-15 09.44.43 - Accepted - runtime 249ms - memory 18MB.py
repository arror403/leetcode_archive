class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L=len(arr)
        dp=[0]*(L+1)

        for i in range(1,L+1):
            curMax=best=0
            j=1
            while(j<=k and (i-j)>=0):
                curMax=max(curMax, arr[i-j])
                best=max(best, dp[i-j]+curMax*j)
                j+=1
            
            dp[i]=best
        

        return dp[L]