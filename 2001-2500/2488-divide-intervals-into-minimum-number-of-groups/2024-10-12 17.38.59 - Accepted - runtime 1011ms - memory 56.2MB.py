class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        end_ptr=res=0
        start_times=sorted([x[0] for x in intervals])
        end_times=sorted([x[1] for x in intervals])

        for s in start_times:
            if s>end_times[end_ptr]:
                end_ptr+=1
            else:
                res+=1


        return res