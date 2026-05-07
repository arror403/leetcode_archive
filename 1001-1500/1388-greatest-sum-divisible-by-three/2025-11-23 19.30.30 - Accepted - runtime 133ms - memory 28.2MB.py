class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        L=len(nums)
        dp = [[0]*3 for _ in range(L+1)]
        dp[0][1] = dp[0][2] = -inf

        for i in range(1, L+1):
            pre = i-1
            for j in range(3):
                dp[i][j] = max(dp[pre][j], dp[pre][(nums[pre]+j)%3]+nums[pre])


        return dp[L][0]