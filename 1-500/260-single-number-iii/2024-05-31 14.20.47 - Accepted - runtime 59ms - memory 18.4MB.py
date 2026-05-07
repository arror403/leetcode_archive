class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        m = reduce(xor, nums, 0)
        x = reduce(xor, [n for n in nums if n&m&(-m)], 0)
        return [x, x^m]