class Solution:
    def concatHex36(self, n: int) -> str:
        t=n**3
        h=[]
        while t:
            h.append(t%36)
            t//=36

        tmp=''
        for v in reversed(h):
            if v>9:
                tmp+=chr(v+55)
            else:
                tmp+=str(v)


        return hex(n**2)[2:].upper()+tmp