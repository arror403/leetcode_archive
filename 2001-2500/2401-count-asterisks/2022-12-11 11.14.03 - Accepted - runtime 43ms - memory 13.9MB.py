class Solution:
    def countAsterisks(self, s: str) -> int:
        res,c=0,0
        for i in list(s):
            if i=='|': c+=1
            if c%2==0 and i=='*': res+=1
        return res