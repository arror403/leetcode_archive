class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        L=len(nums)
        t=[nums[i:j] for i in range(L) for j in range(i+1,L+1)]
        res=[[reduce(lambda x,y: x|y, i),len(i)] for i in t]
        for a,b in sorted(res, key=lambda x:x[1]):
            if a>=k: return b

        return -1