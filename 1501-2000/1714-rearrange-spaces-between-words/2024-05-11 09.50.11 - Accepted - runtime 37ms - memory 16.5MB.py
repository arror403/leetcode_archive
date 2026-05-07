class Solution:
    def reorderSpaces(self, t: str) -> str:
        l=sum(1 for i in t if i==" ")
        if l==0: return t

        t=t.split()
        L=len(t)-1
        if L==0: return t[0]+" "*l

        res=""
        a,b=divmod(l,L)
        
        for x in range(L):
            res+=t[x]
            res+=" "*a

        res+=t[-1]
        res+=" "*b

        return res