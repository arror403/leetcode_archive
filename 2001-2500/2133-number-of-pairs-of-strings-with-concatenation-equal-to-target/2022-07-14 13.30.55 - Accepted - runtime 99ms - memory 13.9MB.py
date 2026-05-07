class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        t=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    t+=1
                if nums[j]+nums[i]==target:
                    t+=1
                    
        return t