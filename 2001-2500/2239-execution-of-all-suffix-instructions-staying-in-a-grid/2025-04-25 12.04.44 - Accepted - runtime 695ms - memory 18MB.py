class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        d = {"R": [0, 1], "D": [1, 0], "U": [-1, 0], "L": [0, -1]}
        res = []
        
        for i in range(len(s)):
            count = 0
            row, col = startPos[0], startPos[1]  # Reset position for each suffix
            
            for j in range(i, len(s)):
                direction = s[j]
                row += d[direction][0]
                col += d[direction][1]
                
                # Check if the robot is still within the grid
                if 0 <= row < n and 0 <= col < n:
                    count += 1
                else:
                    break  # Robot falls off the grid
            
            res.append(count)
        

        return res