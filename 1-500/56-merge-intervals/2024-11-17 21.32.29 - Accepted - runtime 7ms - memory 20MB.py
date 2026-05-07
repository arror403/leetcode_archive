class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<=1: return intervals

        intervals.sort(key=lambda x:x[0])
        ni=intervals[0]
        res=[ni]

        for i in intervals:
            if i[0]<=ni[1]: 
                ni[1]=max(ni[1], i[1])
            else:  
                ni=i
                res.append(ni)


        return res