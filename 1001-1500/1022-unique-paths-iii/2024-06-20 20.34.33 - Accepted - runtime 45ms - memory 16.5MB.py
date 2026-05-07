class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # @lru_cache(maxsize=None)
        def backtrack(x, y, remain):
            # If we are out of bounds or on an obstacle or a visited cell, return 0
            if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == -1:
                return 0
            # If we reach the end cell, check if all non-obstacle cells are visited
            if grid[x][y] == 2:
                return 1 if remain == 1 else 0
            
            # Mark the cell as visited by setting it to -1
            temp = grid[x][y]
            grid[x][y] = -1
            
            # Explore the 4 possible directions
            paths = (backtrack(x + 1, y, remain - 1) +
                    backtrack(x - 1, y, remain - 1) +
                    backtrack(x, y + 1, remain - 1) +
                    backtrack(x, y - 1, remain - 1))
            
            # Unmark the cell (backtrack)
            grid[x][y] = temp
            return paths

        rows, cols = len(grid), len(grid[0])
        empty = 0
        start_x = start_y = end_x = end_y = 0

        # Find the start and end positions and count empty cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    start_x, start_y = r, c
                elif grid[r][c] == 2:
                    end_x, end_y = r, c
                if grid[r][c] != -1:
                    empty += 1
        
        # Use backtracking to explore all paths from the start position
        return backtrack(start_x, start_y, empty)