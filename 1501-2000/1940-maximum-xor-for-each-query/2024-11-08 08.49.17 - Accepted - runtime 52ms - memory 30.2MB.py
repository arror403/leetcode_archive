class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        L=len(nums)
        res=[0]*L
        max_xor=2**maximumBit-1
        
        xor_all=reduce(operator.xor, nums)
        
        for i in range(L):
            res[i]=max_xor^xor_all
            xor_all^=nums.pop()


        return res