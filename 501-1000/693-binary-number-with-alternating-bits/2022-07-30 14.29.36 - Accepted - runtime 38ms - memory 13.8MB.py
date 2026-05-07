class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n,f=(bin(n)[2:]),True
        for i in range(1,len(n)):
            if n[i-1]!=n[i]:
                continue
            else:
                f=False
                break
                
        return f