class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        unique_chars = set()
        l=len(nums)
        for i in range(l):
            unique_chars.clear()  # Clear the unique characters for each new starting position
            for j in range(i, l):
                if nums[j] not in unique_chars:
                    unique_chars.add(nums[j])
                total_sum += len(unique_chars)**2
        
        return total_sum