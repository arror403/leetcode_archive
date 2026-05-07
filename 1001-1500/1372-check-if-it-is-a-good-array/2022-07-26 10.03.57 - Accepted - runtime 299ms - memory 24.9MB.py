class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return 1 if self.find_gcd(nums)==1 else 0
        
    
    def find_gcd(self,l):
        return reduce(gcd, l)