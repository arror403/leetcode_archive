class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s=list(s)
        d={}
        for i in list(dict.fromkeys(s)): d[i]=0
        
        for i in s:
            d[i]+=1
            if d[i]==2: return i