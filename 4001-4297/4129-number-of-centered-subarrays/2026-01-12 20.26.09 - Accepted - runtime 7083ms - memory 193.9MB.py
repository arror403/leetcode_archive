class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        s=[nums[i:j+1] for i in range(len(nums)) for j in range(i, len(nums))]

        return len([v for v in s if sum(v) in v])