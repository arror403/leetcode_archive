class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [v for v,f in Counter(nums).items() if f>1]