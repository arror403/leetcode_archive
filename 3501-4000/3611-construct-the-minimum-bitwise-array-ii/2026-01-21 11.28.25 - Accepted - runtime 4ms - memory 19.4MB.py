class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res=[]

        for v in nums:
            r = -1
            d = 1
            while v & d:
                r = v - d
                d <<= 1

            res.append(r)


        return res