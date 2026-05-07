class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        L=len(nums)//2
        d=[k for k,v in Counter(nums).items() if v>L]
        return d[0]