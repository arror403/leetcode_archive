class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all([x<=2 for x in Counter(nums).values()])