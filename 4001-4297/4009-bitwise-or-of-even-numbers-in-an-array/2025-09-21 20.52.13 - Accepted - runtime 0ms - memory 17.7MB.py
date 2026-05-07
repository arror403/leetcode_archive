class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        return reduce(operator.or_ , m) if (m:=[v for v in nums if v%2==0]) else 0