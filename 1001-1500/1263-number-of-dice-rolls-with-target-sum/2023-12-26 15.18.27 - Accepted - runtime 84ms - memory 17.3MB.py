class Solution:
    def numRollsToTarget(self, n: int, k: int, x: int) -> int:
        mod = 10**9 + 7

        # Initialize a 1D array to store the results
        dp = [0] * (x + 1)
        dp[0] = 1  # Base case: there is one way to get a sum of 0 with 0 dice

        # Fill in the table using the recurrence relation
        for i in range(1, n + 1):
            new_dp = [0] * (x + 1)
            prefix_sum = 0

            for j in range(1, x + 1):
                prefix_sum = (prefix_sum + dp[j - 1]) % mod
                if j - k - 1 >= 0:
                    prefix_sum = (prefix_sum - dp[j - k - 1] + mod) % mod

                new_dp[j] = prefix_sum

            dp = new_dp

        # The answer is stored in dp[x]
        return dp[x]