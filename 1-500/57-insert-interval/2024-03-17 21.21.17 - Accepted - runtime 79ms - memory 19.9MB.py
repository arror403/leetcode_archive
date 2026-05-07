class Solution:
    ##### improved by chatGPT #####
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        merged=[]
        inserted=False

        for i in intervals:
            if i[1]<newInterval[0]:  # If current interval ends before newInterval starts
                merged.append(i)
            elif i[0]>newInterval[1]:  # If newInterval ends before current interval starts
                if not inserted:
                    merged.append(newInterval)
                    inserted=True
                merged.append(i)
            else:  # If there's overlap between current interval and newInterval
                newInterval=[min(i[0],newInterval[0]), max(i[1],newInterval[1])]

        if not inserted: merged.append(newInterval)

        return merged