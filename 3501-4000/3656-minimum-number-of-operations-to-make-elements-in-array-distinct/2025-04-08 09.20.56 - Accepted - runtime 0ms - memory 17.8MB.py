class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        while nums:
            if len(nums)==len(set(nums)):
                return res
            else:
                nums=nums[3:]
                res+=1


        return res