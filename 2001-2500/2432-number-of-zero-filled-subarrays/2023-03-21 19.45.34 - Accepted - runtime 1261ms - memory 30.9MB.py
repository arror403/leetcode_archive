class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums=[list(y) for x,y in groupby(list(nums))]
        # print(m)
        res=0
        for i in nums:
            if set(i)=={0}:
                res+=self.helper(len(i))
                
        
        return res
        
        
    def helper(self, x):
        return int((x+1)*x/2)