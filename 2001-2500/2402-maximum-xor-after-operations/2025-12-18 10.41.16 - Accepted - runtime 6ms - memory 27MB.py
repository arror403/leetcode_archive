class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(operator.or_, [0]+nums)