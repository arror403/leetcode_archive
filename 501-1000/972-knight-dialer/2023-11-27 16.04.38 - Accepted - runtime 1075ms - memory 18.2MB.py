class Solution:
    def knightDialer(self, N: int) -> int:


        ########## power by chatGPT ##########


        if N == 1: return 10
        
        # Define the valid moves for each digit
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        # Initialize a 2D array to store the number of ways for each digit at each step
        dp = [[0] * 10 for _ in range(N)]
        
        # Initialize the base case for N = 1
        for i in range(10):
            dp[0][i] = 1
        
        # Fill the dp array using the recurrence relation
        for step in range(1, N):
            for i in range(10):
                for move in moves[i]:
                    dp[step][i] += dp[step - 1][move]
                    dp[step][i] %= (10**9 + 7)
        
        # Sum up the number of ways for each digit at the last step
        result = sum(dp[N-1]) % (10**9 + 7)
        
        return result