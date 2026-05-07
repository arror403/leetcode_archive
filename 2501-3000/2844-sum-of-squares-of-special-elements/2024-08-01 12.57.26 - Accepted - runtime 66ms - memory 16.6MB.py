class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(v**2 for i,v in enumerate(nums) if len(nums)%(i+1)==0)