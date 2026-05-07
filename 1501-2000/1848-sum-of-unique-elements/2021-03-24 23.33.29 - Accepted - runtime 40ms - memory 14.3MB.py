class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        b=[]
        for i in range(0,len(nums)):
            f=1
            for j in range(0,len(nums)):
                if (nums[i]==nums[j])&(i!=j):
                    f=0
                    break
            if f==1:
                b.append(nums[i])
        if len(b)==0: return 0
        else: return sum(b)
        # print (b)