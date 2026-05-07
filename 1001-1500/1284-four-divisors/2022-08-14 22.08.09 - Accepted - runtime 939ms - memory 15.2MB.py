class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            if len(self.factors(i))==4: 
                res+=sum(list(self.factors(i)))
                
        return res
        
        
        
    def factors(self, n):    
        return set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))