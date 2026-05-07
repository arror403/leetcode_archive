class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        t = 0

        for v in nums:
            t = ((t<<1)+v)%5
            res += [False] if t else [True]
            

        return res