class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        ##### power by Bing #####

        res = 0
        dp = [{} for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j].get(diff, 0)
                dp[i][diff] = dp[i].get(diff, 0) + count + 1
                res += count
        return res