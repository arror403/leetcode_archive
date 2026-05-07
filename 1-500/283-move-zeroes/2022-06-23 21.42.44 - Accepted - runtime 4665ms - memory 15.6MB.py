class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        t=0
        for i in range(len(nums)):
            if nums[i]==0:
                t+=1
                nums.append(0)
        n=0
        while t!=0:
            for i in range(len(nums)):
                if nums[i]==0:
                    del nums[i]
                    t-=1
                    break
                
            
            