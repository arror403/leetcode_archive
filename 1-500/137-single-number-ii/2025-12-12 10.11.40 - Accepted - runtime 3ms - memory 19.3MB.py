class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=b=0
        for v in nums:
            a=(a^v)&(~b)
            b=(b^v)&(~a)

        return a