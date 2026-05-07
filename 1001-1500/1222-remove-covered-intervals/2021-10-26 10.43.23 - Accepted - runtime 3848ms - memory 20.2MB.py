class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        b=[]

        for i in range(len(intervals)):
            for j in range(i+1,len(intervals)):
                if intervals[i][0]>=intervals[j][0] and intervals[i][1]<=intervals[j][1]:
                    b.append(intervals[i])
                if intervals[i][0]<=intervals[j][0] and intervals[i][1]>=intervals[j][1]:
                    b.append(intervals[j])
        
        
        for i in b:
            if i in intervals:
                intervals.remove(i)

        return len(intervals)