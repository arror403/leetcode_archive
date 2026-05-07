class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)+1):
            tmp=0
            for j in nums:
                if j>=i: tmp+=1
            if tmp==i: return i
            
        return -1