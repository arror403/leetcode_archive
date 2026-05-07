class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        L = len(nums) // 2
        nums = sorted([x**2 for x in nums])

        return sum(nums[L:]) - sum(nums[:L])