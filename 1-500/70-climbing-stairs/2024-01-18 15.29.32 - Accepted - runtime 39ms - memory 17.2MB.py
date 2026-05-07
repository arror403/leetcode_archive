class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1
        q=sqrt(5)
        phi = (1 + q) / 2
        return round((phi ** n) / q)