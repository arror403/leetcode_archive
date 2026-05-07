class Solution:
    def rob(self, nums: List[int]) -> int:
        nums=tuple(nums)

        @lru_cache(maxsize=None)
        def houseRobber(n, i):
            if i<0: return 0
            # n[i]+houseRobber(n,i-2):
            # Rob the current house, skip the next one

            # houseRobber(n,i-1):
            # Skip the current house, move to the next one
            return max(n[i]+houseRobber(n,i-2), houseRobber(n,i-1))


        return houseRobber(nums, len(nums)-1)