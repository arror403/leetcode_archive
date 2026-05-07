class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        m=[0,0]
        for v in nums:
            if v==0: continue
            else: m[v>0]+=1

        return max(m)