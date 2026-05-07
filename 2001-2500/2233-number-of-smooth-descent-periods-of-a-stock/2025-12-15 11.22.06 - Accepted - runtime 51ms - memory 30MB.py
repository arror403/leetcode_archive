class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res=0
        n=1
        
        for i in range(1, len(prices)):
            if prices[i]==(prices[i-1]-1):
                n+=1
            else:
                res+=n*(n+1)//2
                n=1
        
        res+=n*(n+1)//2
        

        return res