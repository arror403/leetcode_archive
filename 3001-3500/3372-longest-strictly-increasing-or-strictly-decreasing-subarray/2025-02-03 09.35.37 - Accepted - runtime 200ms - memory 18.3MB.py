class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        m=[nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
        res=1

        for s in m:
            L=len(s)
            if L>1:
                if all(a>b for a,b in pairwise(s)):
                    res=max(res,L)
                if all(a<b for a,b in pairwise(s)):
                    res=max(res,L)


        return res