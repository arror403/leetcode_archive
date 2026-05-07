class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        f=False
        x=0
        if len(t)>len(s):
            return 0
        if len(t) == 0:
            return 1
        else:
            for i in s:
                if x<len(s) and t[x]==i:
                    x+=1
                if x==len(t):
                    f=True
                    break
        return f