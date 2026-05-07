class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        return max(accumulate([0]+nums))-min(accumulate([0]+nums))