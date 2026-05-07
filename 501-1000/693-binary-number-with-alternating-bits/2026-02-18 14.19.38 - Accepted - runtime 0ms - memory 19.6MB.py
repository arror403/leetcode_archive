class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return all(a!=b for a,b in pairwise(bin(n)[2:]))