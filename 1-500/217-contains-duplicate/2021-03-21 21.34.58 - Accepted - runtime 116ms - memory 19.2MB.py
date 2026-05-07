class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag=0
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                flag=1
                break
        return flag