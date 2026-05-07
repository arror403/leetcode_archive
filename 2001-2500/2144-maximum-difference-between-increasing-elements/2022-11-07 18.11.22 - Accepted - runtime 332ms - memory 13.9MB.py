class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res=-inf
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                tmp=nums[j]-nums[i]
                if tmp>res:
                    res=tmp
        return res if res>0 else -1