class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        K=k//2
        
        if n<=K: return n*(n+1)//2
        
        m=n-K

        return K*(K+1)//2 + m*(m+1)//2 + m*(k-1)