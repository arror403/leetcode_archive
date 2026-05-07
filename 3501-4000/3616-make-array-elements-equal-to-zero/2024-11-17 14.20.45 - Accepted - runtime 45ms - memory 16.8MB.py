class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        m=[i for i,v in enumerate(nums) if v==0]
        res=0

        for e in m:
            l,r=sum(nums[:e]),sum(nums[e+1:])
            if l==r:
                res+=2
            elif abs(l-r)==1:
                res+=1


        return res