class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        n=list(map(int,str(n)))
        L=len(n)-1
        i=0
        res=[]

        while L>=0:
            if n[i]: res.append(n[i] * 10**L)
            i+=1
            L-=1

        
        return res