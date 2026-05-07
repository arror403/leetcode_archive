class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        r=[]
        while n>=3:
            r.append(n%3)
            n//=3
        r.append(n)
        # r.reverse()
        
        for i in r:
            if i==1 or i==0: continue
            else: return False
        
        return True