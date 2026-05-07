class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row0=[r.count(0) for r in grid]
        row1=[sum(r) for r in grid]
        col0=[c.count(0) for c in zip(*grid)]
        col1=[sum(c) for c in zip(*grid)]


        return [[row1[i]+col1[j]-row0[i]-col0[j] for j in range(len(grid[0]))] for i in range(len(grid))]