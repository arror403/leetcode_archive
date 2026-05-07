class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        # Create a list to store the number of candies each child gets
        candies = [1] * n
        
        # First pass: Check from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Second pass: Check from right to left and make adjustments
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up the total number of candies distributed
        total_candies = sum(candies)
        
        return total_candies