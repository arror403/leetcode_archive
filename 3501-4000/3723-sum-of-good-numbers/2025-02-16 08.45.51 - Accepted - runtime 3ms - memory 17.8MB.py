class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res=0
        
        for i,v in enumerate(nums):
            is_good=True
            
            if i-k>=0:
                if v<=nums[i-k]:
                    is_good=False
            
            if i+k<len(nums):
                if v<=nums[i+k]:
                    is_good=False

            if is_good: res+=v
                

        return res