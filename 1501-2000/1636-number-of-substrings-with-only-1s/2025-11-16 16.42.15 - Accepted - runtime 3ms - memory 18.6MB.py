class Solution:
    def numSub(self, s: str) -> int:
        res=0

        for i in s.split('0'):
            l=len(i)
            if l==0: 
                continue
            res+=(1+l)*l//2
            

        return res%(10**9+7)