class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        L=len(nums)
        dp = [[0,0,0] for _ in range(L+1)]
        dp[0][0] = 0
        dp[0][1] = -inf
        dp[0][2] = -inf

        for i in range(1, L+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][(nums[i-1]) % 3] + nums[i-1])
            dp[i][1] = max(dp[i-1][1], dp[i-1][(nums[i-1]+1) % 3] + nums[i-1])
            dp[i][2] = max(dp[i-1][2], dp[i-1][(nums[i-1]+2) % 3] + nums[i-1])


        return dp[L][0]