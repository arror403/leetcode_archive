class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        b=-1
        if nums[0]!=0:
            b=0
        else:    
            for i in range(0,len(nums)-1):
                if nums[i]!=nums[i+1]-1:
                    b=nums[i+1]-1
                    
        if b==-1:
            return nums[-1]+1
        else:
            return b