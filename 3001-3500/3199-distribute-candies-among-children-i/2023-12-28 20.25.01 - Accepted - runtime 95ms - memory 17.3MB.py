class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Initialize a variable to store the total number of ways
        total_ways = 0
        
        # Iterate through all possible values for the first part
        for i in range(min(n, limit) + 1):
            # Calculate the remaining sum after fixing the first part
            remaining_sum = n - i
            
            # Calculate the maximum value the second part can take
            max_second_part = min(remaining_sum, limit)
            
            # Iterate through all possible values for the second part
            for j in range(max_second_part + 1):
                # Calculate the third part
                k = remaining_sum - j
                
                # Check if all parts are within the limit
                if k <= limit:
                    # Increment the total number of ways
                    total_ways += 1
        
        return total_ways