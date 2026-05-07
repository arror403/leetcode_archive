class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=tmp=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                tmp+=nums[i]
            else:
                tmp = nums[i]

            res = max(res,tmp)


        return res