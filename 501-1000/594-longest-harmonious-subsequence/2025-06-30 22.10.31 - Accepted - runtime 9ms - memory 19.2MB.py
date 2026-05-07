class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=Counter(nums)
        return max((d[v]+d[v+1] for v in d if v+1 in d), default=0)