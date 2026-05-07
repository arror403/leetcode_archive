class Solution:
    ##### improved by chatGPT #####
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        res = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 1
                    if i < r - 1 and grid[i + 1][j] == 1:
                        res -= 1
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 1
                    if j < c - 1 and grid[i][j + 1] == 1:
                        res -= 1

        return res