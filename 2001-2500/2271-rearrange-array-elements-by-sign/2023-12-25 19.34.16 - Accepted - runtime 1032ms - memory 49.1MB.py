class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        L=len(nums)
        p,n,res=[],[],[]
        for i in range(L):
            if nums[i]>0: p.append(nums[i])
            else: n.append(nums[i])

        for x in range(L//2):
            res.append(p[x])
            res.append(n[x])

        return res