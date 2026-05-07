class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        return sum(v for v in nums if v in range(10))!=sum(nums)/2