class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        L=len(nums)

        for i in range(L):
            idx=abs(nums[i])-1
            if nums[idx]<0: 
                res.append(idx+1)
            nums[idx]*=-1

        return res

        # return [k for k,v in Counter(nums).items() if v==2]