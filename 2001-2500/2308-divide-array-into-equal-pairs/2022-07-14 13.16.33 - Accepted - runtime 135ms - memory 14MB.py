class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        f=1
        for i in range(0,len(nums),2):
            if nums[i]==nums[i+1]:
                continue
            else:
                f=0
                break
                
        return f