class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # [max(c) for r in grid for c in r]
        tmp=[]
        res=0
        while grid[0]:
            for r in grid:
                t=max(r)
                tmp.append(t)
                r.remove(t)
            res+=max(tmp)
            tmp=[]
        return res