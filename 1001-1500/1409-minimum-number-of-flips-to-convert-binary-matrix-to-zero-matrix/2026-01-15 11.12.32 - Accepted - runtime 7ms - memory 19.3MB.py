class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        # 1. Convert the initial matrix into a single integer (bitmask)
        start_state = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    # Map (i, j) to a bit position: i * m + j
                    start_state |= 1 << (i * m + j)
        
        # 2. Standard BFS Setup
        queue = deque([(start_state, 0)]) # (current_state, steps)
        visited = {start_state}
        
        while queue:
            curr, steps = queue.popleft()
            
            # If state is 0, we found the solution (all lights out)
            if curr == 0:
                return steps
            
            # 3. Try flipping every cell in the matrix
            for i in range(n):
                for j in range(m):
                    
                    # Create the 'next_state' based on current
                    next_state = curr
                    
                    # Identify neighbors (including self) to flip
                    # Directions: center, up, down, left, right
                    for r, c in [(i, j), (i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= r < n and 0 <= c < m:
                            bit_pos = r * m + c
                            # XOR (^) toggles the bit (0->1, 1->0)
                            next_state ^= (1 << bit_pos)
                    
                    # If we haven't seen this state, add to queue
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append((next_state, steps + 1))
                        
        return -1