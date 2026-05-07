class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        L=list(range(n))
        f=1
        while k>=n:
            k-=(n-1)
            f*=-1

        return L[k] if f==1 else L[k*f-1]