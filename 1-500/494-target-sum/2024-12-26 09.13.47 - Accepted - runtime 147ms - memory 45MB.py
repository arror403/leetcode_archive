class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(index, curr_sum):
            # Base case: if we've used all numbers, check if we've reached the target
            if index == len(nums):
                return curr_sum == target
                
            # Try both adding and subtracting the current number
            return dp(index + 1, curr_sum + nums[index]) + \
                   dp(index + 1, curr_sum - nums[index])
        
        
        return dp(0, 0)