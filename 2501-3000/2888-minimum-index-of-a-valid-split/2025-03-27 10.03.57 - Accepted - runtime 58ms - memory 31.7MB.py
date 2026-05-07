class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find majority element using Boyer-Moore Voting Algorithm
        candidate = nums[0]
        count = 0
        for num in nums:
            count = count + 1 if num == candidate else count - 1
            if count == 0:
                candidate = num
                count = 1
        
        # Verify total count and split
        total = nums.count(candidate)
        if total * 2 <= len(nums):
            return -1
        
        left_count = 0
        for i in range(len(nums)):
            left_count += nums[i] == candidate
            if (left_count * 2 > i + 1) and ((total - left_count) * 2 > len(nums) - i - 1):
                return i
        
        return -1