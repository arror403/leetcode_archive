class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        d=[]
        for i in range(len(nums)-1):
            t=nums[i]+nums[i+1]
            d.append(t)
            if d.count(t)==2: return True
        print (d)

        return False