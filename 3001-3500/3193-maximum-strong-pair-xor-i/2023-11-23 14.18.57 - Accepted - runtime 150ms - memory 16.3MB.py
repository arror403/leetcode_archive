class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return max([i^j for i in nums for j in nums if abs(i-j)<=min(i,j)])