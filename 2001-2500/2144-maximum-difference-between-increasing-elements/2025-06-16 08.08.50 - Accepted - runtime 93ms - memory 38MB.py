class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        t=max([b-a for a,b in combinations(nums, 2)])

        return t if t>0 else -1