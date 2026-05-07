class Solution:
    def maxProduct(self, A: List[int]) -> int:  
        r=A[0]
        imax=imin=r

        for i in range(1,len(A)):
            if A[i]<0: imax, imin = imin, imax

            imax=max(A[i], imax*A[i])
            imin=min(A[i], imin*A[i])
            r=max(r, imax)


        return r