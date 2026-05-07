class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        b=[]
        x=0
        for i in range(0,n):
            tmp=start+2*i
            b.append(tmp)
        for j in b:
            x=(x^j)
            
        
        return x