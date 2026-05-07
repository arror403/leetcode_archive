class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        return 0 if n<=k and m<=k else (max(m,n)-k)*k