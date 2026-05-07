class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        tmp=0
        b=[]
        if (len(nums)==1)&(nums[0]==1):
            b.append(1)
        else:
            for i in nums:
                if i==1:
                    tmp+=1
                    b.append(tmp)
                elif i==0:
                    tmp=0
                
        if len(b)==0:return 0
        
        else: return (max(b))