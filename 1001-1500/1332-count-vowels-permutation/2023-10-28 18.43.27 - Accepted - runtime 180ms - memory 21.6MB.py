class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9+7
        # Initialize a 2D array dp to store the counts
        # dp[i][j] represents the count of valid permutations of length i ending with the j-th vowel
        dp = [[0]*5 for _ in range(n+1)]
        
        # Initialize the base case: permutations of length 1
        for i in range(5): dp[1][i] = 1
        
        # Define the transitions based on the vowel rules
        # a -> e
        # e -> a, i
        # i -> a, e, o, u
        # o -> i, u
        # u -> a
        
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % MOD
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % MOD
            dp[i][3] = (dp[i-1][2]) % MOD
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % MOD
        
        return sum(dp[n]) % MOD