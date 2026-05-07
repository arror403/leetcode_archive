class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(0,len(nums)):
            sum = 0
            for j in range(0,len(nums)):
                if(i!=j)&(nums[i]>nums[j]):
                    sum+=1
            b.append(sum)
                    
        return b