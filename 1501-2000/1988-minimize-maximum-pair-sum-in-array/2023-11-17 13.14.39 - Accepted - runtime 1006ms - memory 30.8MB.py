class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        
        left, right = 0, n-1
        maxPairSum = 0
        
        while left < right:
            pairSum = nums[left] + nums[right]
            maxPairSum = max(maxPairSum, pairSum)
            left += 1
            right -= 1
        
        return maxPairSum