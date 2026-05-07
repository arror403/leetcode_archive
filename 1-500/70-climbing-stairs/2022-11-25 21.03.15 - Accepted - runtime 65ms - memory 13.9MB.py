class Solution:
    def climbStairs(self, n: int) -> int:
        n+=1
        x=math.sqrt(5)
        return int((((1+x)/2)**n-((1-x)/2)**n)/x)