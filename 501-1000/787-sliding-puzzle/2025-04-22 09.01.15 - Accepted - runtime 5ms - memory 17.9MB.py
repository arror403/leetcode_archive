class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Convert board to string format and define target state
        target = "123450"
        start = ''.join(str(cell) for row in board for cell in row)
        
        # Define adjacent positions (neighbors) for each position in a 2x3 grid
        # This is more intuitive than the original array of arrays
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS implementation
        queue = deque([(start, 0)])  # (state, moves)
        visited = {start}
        
        while queue:
            curr_state, moves = queue.popleft()
            
            if curr_state == target:
                return moves
            
            # Find position of the empty tile (0)
            zero_pos = curr_state.index('0')
            
            # Try all possible moves
            for neighbor in neighbors[zero_pos]:
                # Create new state by swapping 0 with its neighbor
                new_state = list(curr_state)
                new_state[zero_pos], new_state[neighbor] = new_state[neighbor], new_state[zero_pos]
                new_state = ''.join(new_state)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        
        return -1  # No solution found