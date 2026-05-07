class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = deque()
        
        # Find all land cells and add them to the queue as starting points.
        # We also count the number of land cells to handle edge cases.
        land_cells_count = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    land_cells_count += 1

        if land_cells_count == 0 or land_cells_count == n**2:
            return -1

        # Keep track of the distance from the nearest land.
        # We start at -1 because the loop structure will do one final increment
        # after visiting the last layer of cells.
        distance = -1
        
        # 4  directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # BFS
        while q:
            # Process all nodes at the current distance level in one go.
            # `len(q)` gives us the number of nodes at the current "ripple" level.
            level_size = len(q)
            for _ in range(level_size):
                r, c = q.popleft()
                
                # Explore the neighbors of the current cell
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if the neighbor is within bounds and is a water cell (0)
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        # Mark this water cell as visited by changing it to 1
                        grid[nr][nc] = 1
                        # Add it to the q to be processed in the next level
                        q.append((nr, nc))
            
            distance += 1
            # print(q, distance)


        return distance