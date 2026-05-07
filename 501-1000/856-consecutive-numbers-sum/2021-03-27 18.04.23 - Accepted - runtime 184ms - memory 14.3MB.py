class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        x=N
        sum=1
        k=int((2*x-1/4)**(1/2))
        for i in range(2,k+1):
            tmp=i*(i-1)/2
            if ((x-tmp)%i==0):
                sum+=1
                
        return sum