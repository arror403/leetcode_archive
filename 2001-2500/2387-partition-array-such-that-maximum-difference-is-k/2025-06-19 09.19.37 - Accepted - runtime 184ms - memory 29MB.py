class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res=1 
        M=m=nums[0]
        
        for v in nums:
            m=min(m, v)
            M=max(M, v)
            if (M-m)>k:
                res+=1
                M=m=v
            
        
        return res