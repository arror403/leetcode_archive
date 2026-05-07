class Solution:
    def check(self, nums: List[int]) -> bool:
        m=[]
        for i in nums:
            nums=nums[1:]+nums[:1]
            m.append(nums)
            
        if sorted(nums) in m:
            return True
        else:
            return False