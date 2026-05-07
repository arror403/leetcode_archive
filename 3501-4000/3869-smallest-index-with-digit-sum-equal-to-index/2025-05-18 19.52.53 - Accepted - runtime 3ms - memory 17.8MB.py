class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        return next((i for i,v in enumerate(nums) if i==sum(map(int,str(v)))), -1)