class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        # [1,2,2,5,6,6]
        t=0
        for i in range(0,len(nums),2):
            t+=nums[i]
            
        return t