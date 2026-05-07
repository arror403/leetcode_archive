class Solution:
    def numSteps(self, s: str) -> int:
        res=0
        t=int(s, 2)

        while t!=1:
            if t%2==1:
                t+=1    
            else:
                t>>=1
            res+=1


        return res