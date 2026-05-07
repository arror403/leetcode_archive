class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        m=[[k,list(g)] for k,g in groupby(nums)]

        return sum(((len(g)+1)*len(g))//2 for k,g in m if k==0)