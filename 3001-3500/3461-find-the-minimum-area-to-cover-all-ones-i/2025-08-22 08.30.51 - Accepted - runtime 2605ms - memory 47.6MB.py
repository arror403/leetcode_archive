class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        grid_t=list(zip(*grid))

        a=[i for i in range(len(grid)) if 1 in grid[i]]
        b=[j for j in range(len(grid[0])) if 1 in grid_t[j]]


        return (a[-1]-a[0]+1)*(b[-1]-b[0]+1)