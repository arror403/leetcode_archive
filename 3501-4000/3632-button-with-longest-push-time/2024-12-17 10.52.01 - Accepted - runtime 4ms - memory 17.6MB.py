class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        t=[events[0][1]]+[b-a for a,b in pairwise([e[1] for e in events])]
        tmp=max(t)
        
        res=[]
        for a,b in zip([e[0] for e in events], t):
            if b==tmp:
                res.append(a)

        return min(res)