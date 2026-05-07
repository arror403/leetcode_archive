class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        res=count=l=0
        
        for n in nums:
            count+=(n==maxNum)
            
            while count>=k:
                count-=(nums[l]==maxNum)
                l+=1
                
            res+=l
            

        return res