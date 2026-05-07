class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if x not in f:
                f[x]=x
                return x
            if x!=f[x]:
                f[x]=find(f[x])
            return f[x]
        
        f={}
        
        for i,j in stones: f[find(i)]=find(~j)
        
        return len(stones)-len({find(x) for x in f})