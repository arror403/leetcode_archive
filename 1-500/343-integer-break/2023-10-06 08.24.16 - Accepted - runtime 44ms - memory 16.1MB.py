class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        if n==5:
            return 6
        
        k = n-1
        for i in range(2,n//2):
            b = round(n/i)
            c = (b**(i-1)) * (n-b*(i-1))
            k = max(k,c)
        return k