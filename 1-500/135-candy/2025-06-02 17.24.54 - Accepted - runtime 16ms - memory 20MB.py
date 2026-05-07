class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right to left pass with running total
        total = candies[-1]  # Start with the last element
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total += candies[i]
        
        return total

    # Alternative: Space-optimized O(1) solution (more complex but interesting)
    # def candy_space_optimized(self, ratings: List[int]) -> int:
    #     if not ratings:
    #         return 0
            
    #     n = len(ratings)
    #     total = 1
    #     up = down = peak = 1
        
    #     for i in range(1, n):
    #         if ratings[i] > ratings[i - 1]:
    #             # Ascending
    #             down = 1
    #             up += 1
    #             peak = up
    #             total += up
    #         elif ratings[i] == ratings[i - 1]:
    #             # Equal ratings
    #             up = down = peak = 1
    #             total += 1
    #         else:
    #             # Descending
    #             up = 1
    #             down += 1
    #             total += down
    #             # If the descending sequence is longer than the peak,
    #             # we need to add one more candy to the peak
    #             if down > peak:
    #                 total += 1
        
    #     return total