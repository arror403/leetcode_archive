class Solution:
    ##### power by Claude #####
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_gold = 0

        def backtrack(i, j, gold):
            nonlocal max_gold
            max_gold = max(max_gold, gold)
            temp = grid[i][j]
            grid[i][j] = 0  # Mark as visited

            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    backtrack(x, y, gold + grid[x][y])

            grid[i][j] = temp  # Restore the cell value

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    backtrack(i, j, grid[i][j])

        return max_gold