class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        return max([i[0]^i[1] for i in combinations(set(nums),2) if abs(i[0]-i[1])<=min(i[0],i[1])]+[0])