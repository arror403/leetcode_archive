class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return len(list(filter(lambda x: (x[0]+x[1])<target, itertools.combinations(nums, 2))))