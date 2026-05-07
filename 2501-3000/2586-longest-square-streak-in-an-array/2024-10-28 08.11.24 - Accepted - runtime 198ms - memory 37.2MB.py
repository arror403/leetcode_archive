class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp=defaultdict(int)
        res=0
        nums.sort()

        for i in nums:
            root=int(sqrt(i))
            if root*root==i:
                dp[i]=1+dp[root]
            else:
                dp[i]=1
            
            res=max(res, dp[i])


        return res if res>1 else -1 