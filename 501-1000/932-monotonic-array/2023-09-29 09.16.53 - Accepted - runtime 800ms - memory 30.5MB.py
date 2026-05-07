class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        c1,c2=True,True
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            else:
                c1=False
                break

        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                continue
            else:
                c2=False
                break

        return c1 or c2