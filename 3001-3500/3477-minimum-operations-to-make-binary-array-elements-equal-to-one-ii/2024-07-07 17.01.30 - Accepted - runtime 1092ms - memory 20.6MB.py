class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(1 for a,b in pairwise(nums) if a!=b)+(0 if nums[0] else 1)