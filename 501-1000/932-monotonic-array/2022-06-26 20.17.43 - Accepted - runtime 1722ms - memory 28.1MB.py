class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        fa=1
        fd=1
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                continue
            else:
                fa=0
                break
                
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                fd=0
                break
                
        return (fa or fd)