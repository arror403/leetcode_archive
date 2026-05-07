class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            l, r=nums[i], nums[i]
            for j in range(i,len(nums)):
                l = min(l,nums[j])
                r = max(r,nums[j])
                res+=(r-l)
        return res

#         g,res=0,0
#         while 1:
#             g+=1
#             i=0
#             while (i+g)<len(nums):
#                 print(nums[i:i+g+1])
#                 tmp=nums[i:i+g+1]
#                 res+=max(tmp)-min(tmp)
#                 i+=1
#             if g==(len(nums)-1): break
                
#         return res