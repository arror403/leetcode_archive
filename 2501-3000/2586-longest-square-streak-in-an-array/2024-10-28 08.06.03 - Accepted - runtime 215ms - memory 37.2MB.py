class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp=defaultdict(int)
        res=0
        nums.sort()

        for i in nums:
            root=int(i**0.5)
            if root*root==i:
                dp[i]=1+dp[root]
            else:
                dp[i]=1
            
            res=max(res, dp[i])


        return -1 if res<2 else res