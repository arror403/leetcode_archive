class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        i=len(set(nums))-1
        if nums[0]+nums[1]>nums[2]:
            return ["equilateral","isosceles","scalene"][i]
        else:
            return "none"