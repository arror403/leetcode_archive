class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid[0]),len(grid)
        k=k%(m*n)
        g=list(chain.from_iterable(grid))
        g=g[-k:]+g[:-k]
        res=[]

        x=0
        for _ in range(n):
            res.append(g[x:x+m])
            x+=m


        return res