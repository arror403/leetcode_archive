class Solution:
    def numSteps(self, s: str) -> int:
        res=0
        s=int('0b'+s, 2)

        while s!=1:
            if s%2==0:
                s//=2
                res+=1
            else:
                s+=1
                res+=1

        return res