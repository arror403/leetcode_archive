class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        r,c=[sum(x) for x in grid],[sum(x) for x in zip(*grid)]
        
        return sum(r)-sum(vi==vj==grid[i][j]==1 for i,vi in enumerate(r) for j,vj in enumerate(c))