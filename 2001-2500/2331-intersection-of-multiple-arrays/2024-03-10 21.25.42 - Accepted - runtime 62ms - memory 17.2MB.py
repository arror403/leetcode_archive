class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(reduce(lambda x,y: x&y, [set(i) for i in nums]))