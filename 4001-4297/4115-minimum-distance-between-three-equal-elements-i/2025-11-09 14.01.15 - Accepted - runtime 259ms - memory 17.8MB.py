class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = inf
        for i,j,k in combinations(range(len(nums)), 3):
            if nums[i]==nums[j] and nums[j]==nums[k]:
                res = min(res, (k-i)*2)

        return res if res!=inf else -1