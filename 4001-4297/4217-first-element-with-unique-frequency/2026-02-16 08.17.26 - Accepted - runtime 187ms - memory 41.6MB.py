class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        d=Counter(nums)
        df=Counter(d.values())

        for v in nums:
            if df[d[v]]==1:
                return v

        return -1