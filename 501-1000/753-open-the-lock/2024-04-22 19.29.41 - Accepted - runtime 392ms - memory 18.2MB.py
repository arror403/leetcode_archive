class Solution:

    ##### power by Claude #####

    def openLock(self, deadends: List[str], target: str) -> int:

        # Convert deadends to a set for faster lookup
        dead = set(deadends)
        
        # If the initial state "0000" is in deadends, return -1
        if "0000" in dead:
            return -1
        
        # If the target is "0000", return 0
        if target == "0000":
            return 0
        
        # Initialize a queue and a visited set
        queue = deque([("0000", 0)])
        visited = set(["0000"])
        
        # Perform BFS
        while queue:
            current, turns = queue.popleft()
            
            # Try all possible moves from the current state
            for i in range(4):
                # Increment the digit at position i
                digit_up = current[:i] + str((int(current[i]) + 1) % 10) + current[i+1:]
                
                # Decrement the digit at position i
                digit_down = current[:i] + str((int(current[i]) - 1 + 10) % 10) + current[i+1:]
                
                # Check if the new state is valid
                for next_state in (digit_up, digit_down):
                    if next_state not in dead and next_state not in visited:
                        if next_state == target:
                            return turns + 1
                        visited.add(next_state)
                        queue.append((next_state, turns + 1))
        
        # If no solution is found, return -1
        return -1