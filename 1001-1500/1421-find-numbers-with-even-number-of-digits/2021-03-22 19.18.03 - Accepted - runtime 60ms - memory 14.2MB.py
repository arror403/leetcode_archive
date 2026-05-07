class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        b=[]
        sum=0
        for i in nums:
            tmp=0
            while i!=0:
                tmp+=1
                i=int(i/10)
            b.append(tmp)
            
        print(b)
        
        for j in b:
            if j%2==0:
                sum+=1
                
        return sum