class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        res = 0
        
        for j in range(len(grid[0])):
            for i in range(len(grid)-1):
                curr = grid[i][j]
                next_val = grid[i+1][j]

                if next_val <= curr:
                    res += (curr - next_val + 1)
                    grid[i+1][j] = curr + 1


        return res