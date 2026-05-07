class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        res=[0,0]
        ac=0
        for i,v in enumerate(nums):
            if v%2:
                ac=(ac+1)%2
            if (i+1)%6==0:
                ac=(ac+1)%2
            res[ac]+=v

        return res[0]-res[1]