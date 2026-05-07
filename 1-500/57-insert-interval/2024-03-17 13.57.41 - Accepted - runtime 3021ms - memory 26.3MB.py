class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]

        n=set(range(newInterval[0],newInterval[1]+1))
        tmp=set()
        res=[]

        for i in intervals:
            if set(range(i[0],i[1]+1))&n:
                tmp|=(set(range(i[0],i[1]+1))|n)
            else:
                res.append(i)
    
        tmp=list(tmp)

        if tmp:
            return sorted(res+[[min(tmp),max(tmp)]], key=lambda x:x[0])
        else:
            return sorted(res+[newInterval], key=lambda x:x[0])