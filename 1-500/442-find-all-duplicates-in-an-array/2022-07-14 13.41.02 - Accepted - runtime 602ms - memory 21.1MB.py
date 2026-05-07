class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        b=[]
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                b.append(nums[i])
                    
        return b