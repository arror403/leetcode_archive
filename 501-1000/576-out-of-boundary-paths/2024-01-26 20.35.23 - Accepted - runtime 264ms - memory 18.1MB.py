class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        ##### power by chatGPT #####

        # Define a 3D DP array to store the number of paths
        MOD = 10 ** 9 + 7
        dp = [[[0] * n for _ in range(m)] for _ in range(maxMove + 1)]
        
        # Initialize the DP array for the starting position
        dp[0][startRow][startColumn] = 1
        count = 0
        
        # Define the possible moves (up, down, left, right)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Iterate through the number of moves
        for move in range(maxMove):
            for i in range(m):
                for j in range(n):
                    for dx, dy in moves:
                        x, y = i + dx, j + dy
                        # Check if the new position is within the grid
                        if 0 <= x < m and 0 <= y < n:
                            dp[move + 1][x][y] += dp[move][i][j]
                            dp[move + 1][x][y] %= MOD
                        else:
                            # If the new position is out of bounds, increment the count
                            count += dp[move][i][j]
                            count %= MOD
                            
        return count