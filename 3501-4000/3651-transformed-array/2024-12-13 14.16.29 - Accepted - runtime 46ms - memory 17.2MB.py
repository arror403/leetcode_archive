class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i+v)%len(nums)] if v!=0 else 0 for i,v in enumerate(nums)]