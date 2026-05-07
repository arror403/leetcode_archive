class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        
        for i in list(dict.fromkeys(nums)): d[i]=0
        
        for i in nums:
            d[i]+=1
            if d[i]==2: return i