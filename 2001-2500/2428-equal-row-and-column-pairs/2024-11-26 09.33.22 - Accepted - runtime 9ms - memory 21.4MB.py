class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        t=Counter(zip(*grid))
        d=Counter(tuple(r) for r in grid)
        S=t.keys()&d.keys()
        
        return sum(t[i]*d[i] for i in S)