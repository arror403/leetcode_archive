class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=[]

        while n>=3:
            r.append(n%3)
            n//=3

        r.append(n)
        
        for i in r:
            if not (i==1 or i==0): 
                return False
        
        
        return True