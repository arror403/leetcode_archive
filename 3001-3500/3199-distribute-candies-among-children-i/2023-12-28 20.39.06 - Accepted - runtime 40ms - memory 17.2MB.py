class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return sum(1 for i in range(min(n,limit)+1) for j in range(min(n-i,limit)+1) if (n-i-j)<=limit)