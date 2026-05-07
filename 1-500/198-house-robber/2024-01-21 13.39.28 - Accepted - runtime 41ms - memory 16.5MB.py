class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        for i in nums:
            tmp=a
            a=max(b+i,a)
            b=tmp
        return a