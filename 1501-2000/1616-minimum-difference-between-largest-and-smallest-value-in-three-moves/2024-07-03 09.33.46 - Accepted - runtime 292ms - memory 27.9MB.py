class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<=3: return 0
        
        nums.sort()
        S=[[0], [-1], [1,0], [0,-1], [-2,-1], [2,1,0], [-1,1,0], [-2,-1,0], [-3,-2,-1]]
        res=nums[-1]-nums[0]

        for x in S:
            t=nums[:]
            for i in x: del t[i]
            res=min(t[-1]-t[0], res)
        

        return res