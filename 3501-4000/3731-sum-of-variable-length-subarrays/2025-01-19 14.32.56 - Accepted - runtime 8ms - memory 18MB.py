class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        return sum(sum(nums[max(0,i-v):i+1]) for i,v in enumerate(nums))