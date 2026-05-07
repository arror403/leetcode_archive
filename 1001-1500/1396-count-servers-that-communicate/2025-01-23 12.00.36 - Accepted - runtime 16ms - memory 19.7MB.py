class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r=[sum(x) for x in grid]
        c=[sum(x) for x in zip(*grid)]

        g=0
        for i,vi in enumerate(r):
            for j,vj in enumerate(c):
                if vi==vj==grid[i][j]==1:
                    g+=1
        

        return sum(r)-g