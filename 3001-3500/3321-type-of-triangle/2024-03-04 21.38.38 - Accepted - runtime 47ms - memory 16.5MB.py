class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if sum(nsmallest(2, nums))>max(nums):
            return ["equilateral","isosceles","scalene"][len(set(nums))-1]
        else:
            return "none"