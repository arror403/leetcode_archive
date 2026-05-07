class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(-v if i%2 else v for i,v in enumerate(nums))