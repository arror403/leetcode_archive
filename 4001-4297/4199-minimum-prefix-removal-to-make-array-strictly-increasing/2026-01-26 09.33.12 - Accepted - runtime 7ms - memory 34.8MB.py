class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        n=len(nums)
        i=n-1
        while i and nums[i-1]<nums[i]: i-=1
        return i