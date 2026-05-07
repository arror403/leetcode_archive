class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        current_length = max_length = 0
        
        for v in nums:
            if v==max_num:
                current_length+=1
                max_length=max(max_length, current_length)
            else:
                current_length=0


        return max_length