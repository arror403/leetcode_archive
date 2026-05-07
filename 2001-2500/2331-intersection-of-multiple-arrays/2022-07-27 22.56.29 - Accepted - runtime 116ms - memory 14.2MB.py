class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=set(nums[0])
        for i in nums:
            i=set(i)
            res=i.intersection(res)
            
        return sorted(list(res))