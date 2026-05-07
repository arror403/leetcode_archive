class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0]+nums[1]<=nums[2]: return "none"

        L=len(Counter(nums).keys())

        if L==1: return "equilateral"
        elif L==2: return "isosceles"
        else: return "scalene"