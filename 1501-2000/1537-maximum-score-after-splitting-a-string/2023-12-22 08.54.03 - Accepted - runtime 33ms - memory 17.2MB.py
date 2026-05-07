class Solution:
    def maxScore(self, s: str) -> int:
        res=-inf
        for i in range(1,len(s)):
            tmp=s[:i].count('0')+s[i:].count('1')
            if tmp>res:
                res=tmp
        return res