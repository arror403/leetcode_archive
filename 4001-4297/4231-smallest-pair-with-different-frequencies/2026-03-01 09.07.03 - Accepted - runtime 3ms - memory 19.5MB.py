class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d=Counter(nums)
        x=min(d.keys())

        for v in sorted(d.keys()):
            if d[v] != d[x]:
                return [x,v]

        return [-1,-1]