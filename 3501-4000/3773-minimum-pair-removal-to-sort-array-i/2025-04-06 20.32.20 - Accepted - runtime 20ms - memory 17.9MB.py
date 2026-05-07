class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res=0

        while any(b<a for a,b in pairwise(nums)):
            if len(nums)<=1: break
            res+=1
            S=inf
            ind=[]
            
            for i in range(1,len(nums)):
                tmp=nums[i]+nums[i-1]
                if tmp<S:
                    S=tmp
                    ind.append([i,tmp])
                
            ind.sort(key=lambda x: x[1])

            t=ind[0][0]
            nums[t]=(nums[t]+nums[t-1])
            nums.pop(t-1)
        

        return res