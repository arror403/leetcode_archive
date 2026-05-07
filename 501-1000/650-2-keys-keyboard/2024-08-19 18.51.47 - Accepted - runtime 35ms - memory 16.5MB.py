class Solution:
    def minSteps(self, n: int) -> int:
        if n==1: return 0

        res=0
        d=2
        
        while n>1:
            while n%d==0:
                res+=d
                n//=d
            d+=1
        
        return res

        # res=0
        # for i in range(2,n+1):
        #     while(n%i==0):
        #         res+=i
        #         n//=i

        # return res