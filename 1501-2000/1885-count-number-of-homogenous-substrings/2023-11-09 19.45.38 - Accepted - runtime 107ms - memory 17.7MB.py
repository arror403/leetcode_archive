class Solution:
    def countHomogenous(self, s: str) -> int:
        res=0
        for _,x in groupby(s):
            res+=self.helper(len(list(x)))%(10**9+7)
        
        return res
        
  
    def helper(self, x):
        return int((1+x)*x/2)