class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        res=inf

        for a,b,c in combinations(nums, 3):
            if a<b and b>c:
                res=min(res,(a+b+c))


        return res if res!=inf else -1