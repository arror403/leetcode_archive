class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        b=[]
        for i in range(0,len(index)):
            b.insert(index[i],nums[i])
        return b