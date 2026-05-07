class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        m=sorted(int(i[0:2])*60+int(i[3:5]) for i in timePoints)
        res=min(b-a for a,b in pairwise(m))

        return x if (x:=abs(1440-m[-1]+m[0]))<res else res