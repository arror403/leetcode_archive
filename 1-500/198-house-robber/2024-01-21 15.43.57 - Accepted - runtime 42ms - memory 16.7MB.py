class Solution:
    def rob(self, nums: List[int]) -> int:

        @lru_cache()
        def rrrr(i):
            if i<0: return 0
            return max(rrrr(i-2) + nums[i], rrrr(i-1))


        return rrrr(len(nums)-1)