class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i, res = 0, 0
        L = 2

        while i < (len(nums)-2):
            if (nums[i] + nums[i+1]) == nums[i+2]:
                L += 1
            else:
                res = max(res, L)
                L = 2
            
            i += 1

        res = max(res, L)

        return res