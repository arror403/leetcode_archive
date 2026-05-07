class Solution:
    def maxCoins(self, iNums: List[int]) -> int:
        nums=[1]+[x for x in iNums if x>0]+[1]
        n=len(nums)
        dp=[[0]*n for _ in range(n)]

        for k in range(2, n):
            for l in range(n-k):
                r=l+k
                for i in range(l+1, r):
                    dp[l][r]=max(dp[l][r], nums[l]*nums[i]*nums[r] + dp[l][i] + dp[i][r])


        return dp[0][n-1]