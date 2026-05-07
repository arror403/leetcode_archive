class Solution:
    def maxProduct(self, n: int) -> int:
        return max(a*b for a,b in combinations(map(int,str(n)),2))