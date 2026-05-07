class Solution:
    def climbStairs(self, n: int) -> int:
        q=sqrt(5)
        return int( (((1+q)/2)**(n+1) - ((1-q)/2)**(n+1))/q )