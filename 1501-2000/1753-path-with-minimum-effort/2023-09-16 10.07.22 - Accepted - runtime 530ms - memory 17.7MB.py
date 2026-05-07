class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

      rows, cols = len(heights), len(heights[0])
      # Initialize distance array with infinity except for the source node.
      distance = [[float('inf')] * cols for _ in range(rows)]
      distance[0][0] = 0

      # Priority queue for Dijkstra's algorithm.
      pq = [(0, 0, 0)]  # (effort, row, col)
      
      # Define possible moves (up, down, left, right).
      moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

      while pq:
          effort, row, col = heapq.heappop(pq)
          if row == rows - 1 and col == cols - 1:
              return effort  # Reached the destination.

          for dr, dc in moves:
              new_row, new_col = row + dr, col + dc
              if 0 <= new_row < rows and 0 <= new_col < cols:
                  new_effort = max(effort, abs(heights[row][col] - heights[new_row][new_col]))
                  if new_effort < distance[new_row][new_col]:
                      distance[new_row][new_col] = new_effort
                      heapq.heappush(pq, (new_effort, new_row, new_col))

      return -1  # No path found.