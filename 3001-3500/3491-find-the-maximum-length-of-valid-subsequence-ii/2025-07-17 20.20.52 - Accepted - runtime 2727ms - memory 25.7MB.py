class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[[0]*k for _ in range(k)]
        res=0
        
        for v in nums:
            for j in range(k):
                remainder=v%k
                dp[remainder][j]=max(dp[remainder][j], dp[j][remainder]+1)
                res=max(res, dp[remainder][j])
        

        return res