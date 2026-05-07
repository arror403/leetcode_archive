class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask = 0
        for n in nums:
            bitmask ^= n
        diff = bitmask & (-bitmask)
        x = 0
        for n in nums:
            if n & diff:
                x ^= n
        return [x, x ^ bitmask]
                
                