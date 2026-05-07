class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(maxsize=None)
        def dp(index, curr_sum):
            # Base Cases
            if index < 0: return curr_sum == target
            # Decisions
            positive = dp(index-1, curr_sum + nums[index])
            negative = dp(index-1, curr_sum - nums[index])

            return positive + negative


        return dp(len(nums)-1, 0)