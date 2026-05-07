class Solution:
    ##### power by chatGPT #####
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Marking negative numbers and zeros as n + 1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        # Marking visited indices
        for i in range(n):
            x = abs(nums[i])
            if x <= n:
                nums[x - 1] = -abs(nums[x - 1])
        
        # Finding the first positive missing integer
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        
        # If all integers from 1 to n are present, return n + 1
        return n + 1