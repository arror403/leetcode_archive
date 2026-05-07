class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        return next((i for i in sorted(nums,reverse=True) if -i in nums), -1)