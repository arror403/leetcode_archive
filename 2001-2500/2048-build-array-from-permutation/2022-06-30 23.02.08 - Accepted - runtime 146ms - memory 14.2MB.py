class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        b=[]
        for i in range(len(nums)):
            b.append(nums[nums[i]])
            
        return b