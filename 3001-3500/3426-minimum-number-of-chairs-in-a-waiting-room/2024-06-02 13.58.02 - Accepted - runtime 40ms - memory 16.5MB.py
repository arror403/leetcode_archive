class Solution:
    def minimumChairs(self, s: str) -> int:
        c=0
        res=-1
        for p in s:
            if p=='E': c+=1
            else: c-=1
            res=max(c,res)

        return res