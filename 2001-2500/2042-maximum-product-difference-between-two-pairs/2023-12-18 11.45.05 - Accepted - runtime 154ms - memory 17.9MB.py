class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return (t:=sorted(nums))[-1]*t[-2] - t[0]*t[1]