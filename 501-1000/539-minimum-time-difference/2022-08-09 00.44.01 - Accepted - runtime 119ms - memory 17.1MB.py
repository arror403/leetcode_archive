class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        diff,m=inf,[]
        for i in timePoints: m.append(int(i[0:2])*60+int(i[3:5]))
            
        m.sort()
        
        for i in range(1,len(m)):
            if (m[i]-m[i-1]) < diff:
                diff = (m[i]-m[i-1])
        print(m)
        if abs(1440-m[-1]+m[0]) <diff:
            diff=abs(1440-m[-1]+m[0])
        
        return diff
        
        