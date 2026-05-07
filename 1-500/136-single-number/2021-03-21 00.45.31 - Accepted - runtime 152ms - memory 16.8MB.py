class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        b=0
        if len(nums)==1:return nums[0]
        else:
            for i in range(1,len(nums)-1):
                if (nums[i-1]==nums[i])|(nums[i]==nums[i+1]): continue
                else: b=nums[i]


            if(nums[0]!=nums[1]):
                b=nums[0]

            if(nums[-2]!=nums[-1]):
                b=nums[-1]
        return b