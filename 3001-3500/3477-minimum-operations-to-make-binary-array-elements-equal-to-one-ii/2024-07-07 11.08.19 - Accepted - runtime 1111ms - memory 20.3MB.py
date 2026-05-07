class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums=list(map(bool,nums))
        res=0        
        cur=nums[0]
        res=0 if cur else 1
        
        for i in range(1,len(nums)):
            if nums[i] != cur:
                res+=1
                cur=nums[i]
        
        return res