class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m=[nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
        res=0

        for s in m:
            if len(s)==1:
                res=max(res,s[0])
            elif all(a<b for a,b in pairwise(s)):
                res=max(res,sum(s))


        return res