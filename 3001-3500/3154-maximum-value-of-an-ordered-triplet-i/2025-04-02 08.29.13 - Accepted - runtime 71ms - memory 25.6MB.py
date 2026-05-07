class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        return max([(i-j)*k for i,j,k in combinations(nums, 3)]+[0])