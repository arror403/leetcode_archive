class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        res=[]
        while len(nums)!=0:
            res.append((min(nums)+max(nums))/2)
            nums.remove(max(nums))
            nums.remove(min(nums))
        return len(dict.fromkeys(res))