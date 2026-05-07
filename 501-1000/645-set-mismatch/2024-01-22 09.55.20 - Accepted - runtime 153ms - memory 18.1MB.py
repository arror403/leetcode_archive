class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        L=len(nums)
        res=[-1,-1]
        for i in range(1,L+1):
            if d[i]==1: continue
            elif d[i]==2: res[0]=i
            elif d[i]==0: res[1]=i

        return res