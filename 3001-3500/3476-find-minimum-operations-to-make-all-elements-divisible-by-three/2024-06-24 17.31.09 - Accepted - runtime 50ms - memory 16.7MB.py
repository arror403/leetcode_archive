class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 for i in nums if i%3 in [1,2])