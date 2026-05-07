class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        L = len(nums)
        nums.sort()
 
        return max(nums[i]+nums[L-i-1] for i in range(L//2))