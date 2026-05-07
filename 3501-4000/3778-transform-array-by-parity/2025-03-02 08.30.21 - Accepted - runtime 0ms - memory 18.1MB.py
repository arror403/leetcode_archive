class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return [0]*(len(nums)-(odds:=sum(v%2 for v in nums)))+[1]*odds