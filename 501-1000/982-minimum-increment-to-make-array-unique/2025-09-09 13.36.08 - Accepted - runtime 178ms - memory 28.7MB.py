class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res=need=0

        nums.sort()

        for v in nums:
            res+=max(need-v, 0)
            need=max(need, v)+1
        

        return res