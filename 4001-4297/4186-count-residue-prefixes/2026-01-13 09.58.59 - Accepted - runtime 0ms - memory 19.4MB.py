class Solution:
    def residuePrefixes(self, s: str) -> int:
        res=0
        t=set()

        for i in range(len(s)):
            t.add(s[i])
            if len(t) == (i+1)%3:
                res+=1


        return res