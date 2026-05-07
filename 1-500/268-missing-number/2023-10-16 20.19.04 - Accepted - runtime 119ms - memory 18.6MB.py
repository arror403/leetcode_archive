class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return [x for x in {i for i in range(len(nums)+1)}-set(nums)][0]