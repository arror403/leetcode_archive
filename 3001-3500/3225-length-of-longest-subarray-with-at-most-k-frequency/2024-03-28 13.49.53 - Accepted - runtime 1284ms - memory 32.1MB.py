class Solution:
    #ref: https://walkccc.me/LeetCode/problems/2958/
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res=0
        l=0
        c=Counter()

        for r,v in enumerate(nums):
            c[v]+=1
            while c[v]==(k+1):
                c[nums[l]]-=1
                l+=1

            res=max(res, r-l+1)

        return res


        #VVVVVV tried TLE sol. VVVVVV#

        # L=len(nums)
        # d=Counter()
        # res=0
        # start=0
        
        # for end in range(L):
        #     d[nums[end]]+=1
        #     while any(x>k for x in d.values()):
        #         d[nums[start]]-=1
        #         if d[nums[start]]==0: del d[nums[start]]
        #         start+=1
            
        #     if (end-start+1)>res: res=(end-start+1)
            
        # return res