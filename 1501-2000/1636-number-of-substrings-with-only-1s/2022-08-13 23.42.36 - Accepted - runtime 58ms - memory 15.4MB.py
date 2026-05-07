class Solution:
    def numSub(self, s: str) -> int:
        # print(len(s))
        s=s.split('0')
        res=0
        # print(len(s))
        for i in s:
            if len(i)==0: continue
            res+=self.helper(len(i))
            
        return res%(10**9+7)
        
        
        
        
    def helper(self, x):
        return int((1+x)*x/2)