class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j])==target:
                    b.append(i)
                    b.append(j)
        b.sort()    
        return (b)