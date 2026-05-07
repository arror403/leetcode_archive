class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        f=False
        if len(nums)==1 and nums[0]==1:
            f=True
        elif min(nums)==1:
            f=True
        else:
            if self.find_gcd(nums)==1:
                f=True
            else:
                f=False
        return f
    
        # print(self.find_gcd(nums))
        
        
    
    def find_gcd(self,l):
        x = reduce(gcd, l)
        return x