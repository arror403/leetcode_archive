class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = reduce(xor, nums, 0)
        diff = bitmask&(-bitmask)
        x = reduce(xor, [n for n in nums if n&diff], 0)
        return [x, x^bitmask]