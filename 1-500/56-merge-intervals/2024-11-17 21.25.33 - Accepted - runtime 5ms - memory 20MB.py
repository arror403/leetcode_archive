class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1: return intervals

        res=[]
        intervals.sort(key=lambda x:x[0])
        newInterval=intervals[0]
        res.append(newInterval)
        
        for i in intervals:
            #Overlapping intervals, move the end if needed
            if i[0]<=newInterval[1]: 
                newInterval[1]=max(newInterval[1], i[1])
            # Disjoint intervals, add the new interval to the list
            else:  
                newInterval=i
                res.append(newInterval)


        return res