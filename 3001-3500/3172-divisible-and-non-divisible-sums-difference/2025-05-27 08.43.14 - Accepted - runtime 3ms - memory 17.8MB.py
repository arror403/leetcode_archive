class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s=[[],[]]
        for i in range(1,n+1): s[(i%m)>0]+=[i]

        return sum(s[1])-sum(s[0])