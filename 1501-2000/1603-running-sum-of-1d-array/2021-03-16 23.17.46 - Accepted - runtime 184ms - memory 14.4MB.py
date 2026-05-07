class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # a = input()
        # a = a.split(' ')
        b=[]

        for i in range(0,len(nums)):
            sum=0
            for j in range(0,i+1):
                sum=sum+int(nums[j])
            b.append(sum)    

        return b