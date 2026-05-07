class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=domi_num=0

        for v in nums:
            if cnt==0:
                domi_num=v
            cnt+=1 if domi_num==v else -1

        tot=nums.count(domi_num)
        if n==tot*2-1: return -1
        
        cnt=0

        for i,v in enumerate(nums):
            if v==domi_num:
                cnt+=1
            if cnt*2>i+1 and (tot-cnt)*2>n-i-1:
                return i


        return -1