class Solution:
    def specialArray(self, nums: List[int]) -> int:
        return next((i for i in range(1,len(nums)+1) if sum(1 for j in nums if j>=i)==i), -1)