class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        S = sum(nums)
        L = len(nums)
        res = 0

        for v in nums:
            if (L-1) and v > (S-v)/(L-1): res += 1
            S -= v
            L -= 1


        return res