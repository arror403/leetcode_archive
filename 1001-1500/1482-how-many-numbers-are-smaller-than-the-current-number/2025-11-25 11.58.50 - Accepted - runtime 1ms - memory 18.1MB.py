class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = defaultdict(list)
        for i,v in enumerate(sorted(nums)): d[v].append(i)

        return [min(d[v]) for v in nums]