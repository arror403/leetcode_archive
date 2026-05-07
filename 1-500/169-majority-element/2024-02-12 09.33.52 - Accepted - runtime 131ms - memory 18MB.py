class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return next(k for k,v in Counter(nums).items() if v>len(nums)//2)