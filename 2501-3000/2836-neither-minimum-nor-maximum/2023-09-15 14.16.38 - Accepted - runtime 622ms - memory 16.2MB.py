class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        t=[i for i in nums if (i!=min(nums) and i!=max(nums))]
        return t[0] if t else -1