class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(0,len(nums)):
            if i%2==1: continue
            else:
                for j in range(0,nums[i]):
                    b.append(nums[i+1])
                    
        return b