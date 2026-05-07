class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        d=defaultdict(int)

        for c,v in zip(s,cost): d[c]+=v

        d=sorted(d.items(), key=lambda x:x[1])
        
        d.pop()


        return sum(x[1] for x in d)