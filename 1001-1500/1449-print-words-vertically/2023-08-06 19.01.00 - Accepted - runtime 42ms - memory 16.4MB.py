class Solution:
    def printVertically(self, s: str) -> List[str]:
        t=s.split()
        l=0
        res=[]
        for i in t:
            tmp=len(i)
            if tmp>l:
                l=tmp

        for i in range(l):
            tmp=[]
            for j in t:
                if i<len(j):
                    tmp.append(j[i])
                else:
                    tmp.append(' ')
            res.append((''.join(tmp)).rstrip())

        return res