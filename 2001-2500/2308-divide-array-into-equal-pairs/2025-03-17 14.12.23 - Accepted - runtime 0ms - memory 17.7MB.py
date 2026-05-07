class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(f%2==0 for f in Counter(nums).values())