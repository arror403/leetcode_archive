class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums)<=2: return 0
        
        count=0
        nums.sort()
        
        for k in range(2,len(nums)):
            i,j=0,k-1
            while i<j:
                if nums[i]+nums[j]>nums[k]:
                    count+=(j-i)
                    j-=1
                else:
                    i+=1


        return count