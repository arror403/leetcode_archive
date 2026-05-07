class Solution:
    def countHomogenous(self, s: str) -> int:
        m = [list(y) for x, y in groupby(list(s))]
        res=0
        for i in m: res+=self.helper(len(i))
        
        return res%(10**9+7)
        
    
    
    
    
    def helper(self, x):
        return int((1+x)*x/2)