class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        res = n-1  # worst case: keep only 1 element
        
        for i in range(n):
            right = bisect_right(nums, nums[i]*k)-1
            kept = right-i+1 # number of elements we can keep
            res = min(res, n-kept)
        

        return res