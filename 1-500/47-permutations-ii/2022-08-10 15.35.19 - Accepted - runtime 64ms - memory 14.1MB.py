class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return dict.fromkeys(itertools.permutations(nums))