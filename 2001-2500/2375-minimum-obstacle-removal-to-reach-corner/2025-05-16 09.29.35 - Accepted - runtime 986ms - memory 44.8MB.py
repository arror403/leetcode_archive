class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        # Initialize dp array with maximum values
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        
        # Four directions: right, left, down, up
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        # Use deque instead of priority queue for 0-1 BFS
        queue = deque()
        queue.append((0, 0, 0))  # (row, col, cost)
        dp[0][0] = 0
        
        while queue:
            i, j, cost = queue.popleft()
            
            # If we've reached the destination
            if i == n - 1 and j == m - 1:
                return cost
            
            # If we've found a better path already, skip
            if cost > dp[i][j]:
                continue
            
            # Try all four directions
            for k in range(4):
                new_i, new_j = i + dx[k], j + dy[k]
                
                # Check if the new position is valid and offers a better path
                if 0 <= new_i < n and 0 <= new_j < m:
                    new_cost = cost + grid[new_i][new_j]
                    
                    if new_cost < dp[new_i][new_j]:
                        dp[new_i][new_j] = new_cost
                        
                        # Key optimization: For 0-1 BFS, add to front of queue if cost is 0,
                        # otherwise add to back
                        if grid[new_i][new_j] == 0:
                            queue.appendleft((new_i, new_j, new_cost))
                        else:
                            queue.append((new_i, new_j, new_cost))
        
        # This should not happen if the grid is valid
        return dp[n-1][m-1]