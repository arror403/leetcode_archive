class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        for i in range(32):  # Iterate through each bit position
            count_ones = 0
            
            for num in nums:
                count_ones += (num >> i) & 1
            
            count_zeros = n - count_ones
            total_distance += count_ones * count_zeros
        
        return total_distance