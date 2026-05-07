class Solution:
    def capitalizeTitle(self, s: str) -> str:
        s=s.split()
        s=[list(i.lower()) for i in s]
        res=[]

        for i in s:
            if len(i)<=2:
                res.append(''.join(i))
                continue
            else:
                i[0]=i[0].upper()
                res.append(''.join(i))

        res=' '.join(res)
        
        return res