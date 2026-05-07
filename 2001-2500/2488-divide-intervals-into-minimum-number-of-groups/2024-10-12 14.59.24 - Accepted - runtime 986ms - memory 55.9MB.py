class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        start_times,end_times=[],[]
        end_ptr=group_count=0

        for i in intervals:
            start_times.append(i[0])
            end_times.append(i[1])

        start_times.sort()
        end_times.sort()

        for s in start_times:
            if s>end_times[end_ptr]:
                end_ptr+=1
            else:
                group_count+=1


        return group_count