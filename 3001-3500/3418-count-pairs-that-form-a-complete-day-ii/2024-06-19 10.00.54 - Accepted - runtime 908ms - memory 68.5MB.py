class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        d=Counter([v%24 for v in hours])
        return sum((d[i]*(d[i]-1))//2 for i in [0,12])+sum(d[r]*d[24-r] for r in range(1,12))