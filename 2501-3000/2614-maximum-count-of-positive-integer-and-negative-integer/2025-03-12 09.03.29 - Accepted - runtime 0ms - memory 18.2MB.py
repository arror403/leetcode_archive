class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=bisect_left(nums, 0)
        p=len(nums)-bisect_right(nums, 0)

        return max(n, p)