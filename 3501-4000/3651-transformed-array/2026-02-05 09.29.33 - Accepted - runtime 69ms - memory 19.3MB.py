class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        L=len(nums)
        return [nums[(i+nums[i])%L] if nums[i] else 0 for i in range(L)]