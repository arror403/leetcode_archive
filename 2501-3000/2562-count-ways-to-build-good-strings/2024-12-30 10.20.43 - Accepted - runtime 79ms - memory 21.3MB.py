class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # b=max(zero, one)

        # for i in range(low, high+1):

        dp=[0]*(high+1)
        dp[0]=1
        md=10**9+7
        res=0

        for i in range(min(zero, one), high+1):
            if i>=zero:
                dp[i]=(dp[i]+dp[i-zero])%md
            if i>=one:
                dp[i]=(dp[i]+dp[i-one])%md
            
        for i in range(low, high+1):
            res=(res+dp[i])%md


        return res