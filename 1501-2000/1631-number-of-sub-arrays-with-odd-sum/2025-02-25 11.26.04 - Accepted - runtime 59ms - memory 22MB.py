class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Count of prefix sums with even and odd parity
        even_count = 1  # Start with 1 for empty prefix
        odd_count = 0
        
        result = 0
        current_sum = 0
        
        for num in arr:
            # Update prefix sum parity (0 for even, 1 for odd)
            current_sum = (current_sum + num) % 2
            
            if current_sum == 0:
                # If current prefix sum is even, all previous odd prefixes can form odd sum subarrays
                result = (result + odd_count) % MOD
                even_count += 1
            else:
                # If current prefix sum is odd, all previous even prefixes can form odd sum subarrays
                result = (result + even_count) % MOD
                odd_count += 1
        
        return result