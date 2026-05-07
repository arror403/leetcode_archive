class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set()
        res=0

        for v in nums:
            if v>=0 and v not in s:
                res+=v
                s.add(v)


        return res if s else max(nums)