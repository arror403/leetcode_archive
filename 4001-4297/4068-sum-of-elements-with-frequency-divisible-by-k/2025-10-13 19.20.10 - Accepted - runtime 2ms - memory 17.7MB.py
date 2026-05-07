class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        return sum([v*f for v,f in Counter(nums).items() if f%k==0])