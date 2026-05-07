class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        return sum(int(a + b == target) + int(b + a == target) for a, b in combinations(nums, 2))