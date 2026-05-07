class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n=list(map(int,str(bin(n)[2:])))
        res=[]
        for i in n:
            if i==1: res.append(0)
            else: res.append(1)
        
        return int(''.join([str(i) for i in res]),2)