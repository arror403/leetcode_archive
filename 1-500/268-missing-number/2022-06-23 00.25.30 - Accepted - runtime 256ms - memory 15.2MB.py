class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        f=0
        for i in range(len(nums)+1):
            if i<len(nums):
                if i != nums[i]:
                    f=1
                    return i
                    
        if f==0: return (len(nums))