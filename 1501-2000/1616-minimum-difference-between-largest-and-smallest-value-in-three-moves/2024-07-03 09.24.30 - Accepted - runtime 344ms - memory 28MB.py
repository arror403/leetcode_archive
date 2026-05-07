class Solution:
    def minDifference(self, nums: List[int]) -> int:
        L=len(nums)
        if L<=3: return 0
        nums.sort()
        S=[[0], [L-1], [0,1], [0,L-1], [L-2,L-1], [0,1,2], [0,1,L-1], [0,L-2,L-1], [L-3,L-2,L-1]]
        res=nums[-1]-nums[0]
        # C(6,3)=20, C(4,2)=6, C(2,1)=2, C(6,0)=1
        for x in S:
                t=nums[:]
                for i in reversed(x):
                    del t[i]
                res=min(max(t)-min(t), res)
        

        return res