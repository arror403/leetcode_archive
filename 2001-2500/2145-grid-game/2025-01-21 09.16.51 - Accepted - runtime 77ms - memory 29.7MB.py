class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        topSum, bottomSum = sum(grid[0]), 0
        res = float('inf')

        for i in range(len(grid[0])):
            topSum -= grid[0][i]
            res = min(res, max(topSum, bottomSum))
            bottomSum += grid[1][i]


        return res