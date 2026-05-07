class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        return (a:=nlargest(2,nums))[0]*a[1]-(b:=nsmallest(2,nums))[0]*b[1]