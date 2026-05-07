class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        m=int(len(nums)/2)
        t=0
        for i in range(len(nums)):
            t+=abs(nums[i]-nums[m])
            
        return t