class Solution:
    def clumsy(self, n: int) -> int:
        return [1,2,6,7][n-1] if n in (1,2,3,4) else [n+1,n+2,n+2,n-1][n%4]