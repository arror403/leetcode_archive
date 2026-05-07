class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize a list to store the number of combinations for each amount from 0 to 'amount'
        dp = [0] * (amount + 1)
        
        # Base case: There is one way to make amount 0 (using no coins)
        dp[0] = 1
        
        # Iterate through each coin denomination
        for coin in coins:
            # For each coin, update the dp array to account for the combinations it can contribute
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        # The final result is stored in dp[amount]
        return dp[amount]