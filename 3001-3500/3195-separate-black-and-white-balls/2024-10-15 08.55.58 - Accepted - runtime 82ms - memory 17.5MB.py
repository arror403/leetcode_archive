class Solution:
    def minimumSteps(self, s: str) -> int:
        s=s[::-1]
        res,t=0,0

        for c in s:
            if c=='0':
                t+=1
            else:
                res+=t


        return res