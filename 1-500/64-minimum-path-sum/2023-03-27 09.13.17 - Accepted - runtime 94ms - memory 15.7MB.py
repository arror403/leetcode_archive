class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        
        # Initialize the first row and first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # Calculate the minimum path sum for each cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # Return the minimum path sum for the bottom right cell
        return grid[-1][-1]