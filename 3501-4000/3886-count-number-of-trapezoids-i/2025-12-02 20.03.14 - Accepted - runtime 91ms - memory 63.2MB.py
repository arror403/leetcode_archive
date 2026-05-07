class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        d=defaultdict(int)
        MOD=(10**9+7)
        res=0

        for a,b in points: d[b]+=1

        t=[x*(x-1)//2 for x in d.values()]
        S=sum(t)

        for x in t:
            res+=x*(S-x)
            
        res//=2


        return res%MOD