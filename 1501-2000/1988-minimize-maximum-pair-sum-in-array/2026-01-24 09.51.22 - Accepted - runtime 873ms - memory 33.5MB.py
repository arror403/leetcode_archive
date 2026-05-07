class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        L = len(nums)
        l = L>>1
        
        return max(nums[i]+nums[L-i-1] for i in range(l))