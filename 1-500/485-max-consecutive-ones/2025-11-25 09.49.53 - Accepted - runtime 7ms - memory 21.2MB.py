class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max((len(list(g)) for k,g in groupby(nums) if k), default=0)