class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        up=1
        pre_max_up=res=0
        for i in range(1,n):
            if nums[i]>nums[i-1]: 
                up+=1
            else:
                pre_max_up=up
                up=1
            res=max([res, up //2, min(pre_max_up, up)])


        return res>=k
    # a,b=0,k
    # l,r=nums[:b],nums[b+1:b+k+1]
    # if not(self.isIncreasing(l) or self.isIncreasing(r)): return False

    # while b+k<len(nums):
    #     a+=1
    #     b+=1


    # def isIncreasing(self, s):
    #     for i in range(len(s)-1):
    #         if s[i]>=s[i+1]:
    #             return False
    #     return True