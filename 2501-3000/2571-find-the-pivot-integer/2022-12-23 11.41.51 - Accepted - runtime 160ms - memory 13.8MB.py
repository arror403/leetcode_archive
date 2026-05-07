class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1,n+1):
            # print((1+i)*i/2,(i+n)*(n-i+1)/2)
            if (1+i)*i==(i+n)*(n-i+1): return i
        return -1