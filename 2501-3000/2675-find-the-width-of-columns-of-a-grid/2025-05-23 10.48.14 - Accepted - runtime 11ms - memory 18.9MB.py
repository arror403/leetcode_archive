class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        res=[]

        for c in zip(*grid):
            tmp=-1
            for v in c: tmp=max(tmp, len(str(v)))
            
            res+=[tmp]

        return res