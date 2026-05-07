class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            tmp=[]
            for i in range(1,len(nums)):
                tmp.append((nums[i]+nums[i-1])%10)
                # print(tmp)
            nums=tmp
            
            
        return nums[0]